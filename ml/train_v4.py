"""
Train LegoGPT v4 — 25M params, ~3 hours CPU.

Architecture upgrades from v3:
- d_model 320 -> 512
- n_layers 6 -> 8
- d_ff 1280 -> 2048
- Total ~25M params (3x v3).
- 512 context (same).
- Dropout 0.15 (slightly higher to combat overfit on larger model).

Time budget: 3 hours = 180 minutes.
With 25M params (~3x compute of v3's 7.7M), each epoch takes ~9 min.
180 / 9 = 20 epochs max.
"""
from __future__ import annotations

import json
import math
import time
from pathlib import Path

import torch
from torch.utils.data import Dataset, DataLoader

from ml.model import LegoGPT, ModelConfig


class MPDDatasetV1(Dataset):
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
        vocab_size=512,
        d_model=512,
        n_layers=8,
        n_heads=8,
        d_ff=2048,
        max_seq_len=512,
        dropout=0.15,
    )

    epochs = 20
    batch_size = 8
    peak_lr = 2.5e-4  # slightly lower for bigger model
    min_lr = 2.5e-5
    weight_decay = 0.1
    warmup_steps = 80

    ds = MPDDatasetV1(ml_dir / "dataset.jsonl", cfg.max_seq_len)
    print(f"Dataset: {len(ds)} sequences", flush=True)
    loader = DataLoader(ds, batch_size=batch_size, shuffle=True, num_workers=0)

    model = LegoGPT(cfg)
    print(f"Model params: {model.num_params():,}", flush=True)

    device = torch.device("cpu")
    model.to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=peak_lr, weight_decay=weight_decay, betas=(0.9, 0.95))

    total_steps = epochs * len(loader)
    print(f"Training: {epochs} epochs × {len(loader)} batches = {total_steps} steps", flush=True)

    save_path = ml_dir / "model_v4.pt"
    log_path = ml_dir / "train_v4.log"
    log = []

    step = 0
    t0 = time.time()
    for epoch in range(epochs):
        model.train()
        ep_loss = 0.0
        ep_n = 0
        for x, y in loader:
            x, y = x.to(device), y.to(device)
            lr = get_lr(step, warmup_steps, total_steps, peak_lr, min_lr)
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
            if step % 20 == 0:
                elapsed = time.time() - t0
                eta = elapsed / step * (total_steps - step)
                print(f"  e{epoch+1} step {step:4d}/{total_steps}  loss={loss.item():.4f}  lr={lr:.2e}  elapsed={elapsed:.0f}s eta={eta:.0f}s", flush=True)

        avg_loss = ep_loss / max(ep_n, 1)
        print(f"epoch {epoch+1}/{epochs}  avg_loss={avg_loss:.4f}  elapsed={(time.time()-t0):.0f}s", flush=True)
        log.append({"epoch": epoch + 1, "avg_loss": avg_loss, "step": step})

        torch.save({
            "model": model.state_dict(),
            "cfg": cfg.__dict__,
            "vocab_path": str(ml_dir / "vocab.json"),
            "epoch": epoch + 1,
            "loss": avg_loss,
        }, save_path)

    log_path.write_text("\n".join(json.dumps(r) for r in log))
    print(f"\nSaved {save_path}", flush=True)
    print(f"Total time: {time.time() - t0:.0f}s", flush=True)
    print(f"Final loss: {log[-1]['avg_loss']:.4f}", flush=True)


if __name__ == "__main__":
    main()
