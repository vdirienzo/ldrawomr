"""
Train LegoGPT v5 — Town Specialist.

Focused training on town-themed sets only (159 mid-range sets) with
theme conditioning via THEME_TOWN_* tokens.

Architecture: 88M params (3.4x v4).
  d_model=768, n_layers=12, d_ff=3072, max_seq_len=512, dropout=0.15.
Time estimate: ~5 min/epoch * 25 epochs = ~2 hours CPU.

Supports resume: if ml/model_v5.pt exists, training continues from
the saved epoch. To start fresh, delete the checkpoint.
"""
from __future__ import annotations

import json
import math
import time
from pathlib import Path

import torch
from torch.utils.data import Dataset, DataLoader

from ml.model import LegoGPT, ModelConfig


class MPDDatasetV3(Dataset):
    def __init__(self, jsonl_path: Path, max_seq_len: int):
        self.records = []
        with jsonl_path.open() as f:
            for line in f:
                d = json.loads(line)
                toks = d["tokens"][:max_seq_len]
                self.records.append(toks)
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        toks = self.records[idx]
        x = torch.tensor(toks[:-1] + [0] * (self.max_seq_len - len(toks)), dtype=torch.long)
        y = torch.tensor(toks[1:] + [0] * (self.max_seq_len - len(toks)), dtype=torch.long)
        pad_len = self.max_seq_len - len(toks)
        if pad_len > 0:
            y[-pad_len:] = -100
        return x, y


def get_lr(step, warmup, total, peak_lr, min_lr):
    if step < warmup:
        return peak_lr * (step + 1) / max(warmup, 1)
    if step >= total:
        return min_lr
    progress = (step - warmup) / max(total - warmup, 1)
    return min_lr + 0.5 * (peak_lr - min_lr) * (1 + math.cos(math.pi * progress))


def main():
    base = Path("/home/user/Projects/ldraw")
    ml_dir = base / "ml"

    cfg = ModelConfig(
        vocab_size=2048,
        d_model=768,
        n_layers=12,
        n_heads=12,
        d_ff=3072,
        max_seq_len=512,
        dropout=0.15,
    )

    epochs = 25
    batch_size = 6
    peak_lr = 2e-4
    min_lr = 2e-5
    weight_decay = 0.1
    warmup_steps = 50

    save_path = ml_dir / "model_v5.pt"
    log_path = ml_dir / "train_v5.log"

    # Try to resume from existing checkpoint
    start_epoch = 0
    if save_path.exists():
        ckpt = torch.load(save_path, map_location="cpu", weights_only=False)
        if ckpt.get("cfg") == cfg.__dict__:
            start_epoch = ckpt["epoch"]
            print(f"Resuming from epoch {start_epoch} (saved loss={ckpt['loss']:.4f})", flush=True)
        else:
            print(f"Existing checkpoint has different config, starting fresh", flush=True)

    ds = MPDDatasetV3(ml_dir / "dataset_v3.jsonl", cfg.max_seq_len)
    print(f"Dataset v3 (town-only): {len(ds)} sequences", flush=True)
    loader = DataLoader(ds, batch_size=batch_size, shuffle=True, num_workers=0)

    model = LegoGPT(cfg)
    if start_epoch > 0:
        model.load_state_dict(ckpt["model"])
    print(f"Model params: {model.num_params():,}", flush=True)

    device = torch.device("cpu")
    model.to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=peak_lr, weight_decay=weight_decay, betas=(0.9, 0.95))

    remaining_epochs = epochs - start_epoch
    steps_per_epoch = len(loader)
    total_remaining_steps = remaining_epochs * steps_per_epoch
    print(f"Training: {remaining_epochs} remaining epochs × {steps_per_epoch} batches = {total_remaining_steps} steps", flush=True)
    print(f"Expected: ~5 min/epoch, ~2h total", flush=True)

    # Load existing log if resuming
    log = []
    if log_path.exists():
        try:
            log = [json.loads(l) for l in log_path.read_text().split("\n") if l]
        except Exception:
            log = []

    step = start_epoch * steps_per_epoch
    t0 = time.time()
    for epoch in range(start_epoch, epochs):
        model.train()
        ep_loss = 0.0
        ep_n = 0
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            warmup_total = warmup_steps + start_epoch * steps_per_epoch
            lr = get_lr(step, warmup_total, epochs * steps_per_epoch, peak_lr, min_lr)
            for pg in optim.param_groups:
                pg["lr"] = lr

            _, loss = model(x, y)
            optim.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optim.step()

            ep_loss += loss.item()
            ep_n += 1
            step += 1
            if step % 10 == 0:
                elapsed = time.time() - t0
                eta = elapsed / max(step - start_epoch * steps_per_epoch, 1) * max((epochs - start_epoch) * steps_per_epoch - (step - start_epoch * steps_per_epoch), 1)
                print(f"  e{epoch+1} step {step:3d}/{epochs * steps_per_epoch}  loss={loss.item():.4f}  lr={lr:.2e}  elapsed={elapsed:.0f}s eta={eta:.0f}s", flush=True)

        avg_loss = ep_loss / max(ep_n, 1)
        print(f"epoch {epoch+1}/{epochs}  avg_loss={avg_loss:.4f}  elapsed={(time.time()-t0):.0f}s", flush=True)
        log.append({"epoch": epoch + 1, "avg_loss": avg_loss, "step": step})

        torch.save({
            "model": model.state_dict(),
            "cfg": cfg.__dict__,
            "vocab_path": str(ml_dir / "vocab_v3.json"),
            "epoch": epoch + 1,
            "loss": avg_loss,
        }, save_path)
        # Write log after each epoch (so partial progress is preserved)
        log_path.write_text("\n".join(json.dumps(r) for r in log))

    print(f"\nSaved {save_path}", flush=True)
    print(f"Total time this session: {time.time() - t0:.0f}s", flush=True)
    print(f"Final loss: {log[-1]['avg_loss']:.4f}", flush=True)


if __name__ == "__main__":
    main()
