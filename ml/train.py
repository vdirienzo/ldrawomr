"""
Train the LegoGPT model on the tokenized MPD corpus.

State-of-the-art training choices:
- AdamW with weight decay 0.1 (decoupled regularization).
- Linear warmup + cosine decay schedule.
- Cross-entropy loss with PAD ignored.
- Truncate sequences to max_seq_len for batch uniformity.
"""
from __future__ import annotations

import json
import math
import random
import time
from pathlib import Path

import torch
from torch.utils.data import Dataset, DataLoader

from ml.model import LegoGPT, ModelConfig


class MPDDataset(Dataset):
    def __init__(self, jsonl_path: Path, max_seq_len: int):
        self.records = []
        with jsonl_path.open() as f:
            for line in f:
                d = json.loads(line)
                tokens = d["tokens"][:max_seq_len]
                self.records.append(tokens)
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.records)

    def __getitem__(self, idx):
        toks = self.records[idx]
        # Input: toks[:-1], target: toks[1:]
        x = torch.tensor(toks[:-1] + [0] * (self.max_seq_len - len(toks)), dtype=torch.long)
        y = torch.tensor(toks[1:] + [0] * (self.max_seq_len - len(toks)), dtype=torch.long)
        # Mask out padding positions in target
        pad_len = self.max_seq_len - len(toks)
        y[-pad_len:] = -100
        return x, y


def get_lr(step: int, warmup: int, total: int, peak_lr: float, min_lr: float) -> float:
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
        d_model=256,
        n_layers=6,
        n_heads=8,
        d_ff=1024,
        max_seq_len=512,
        dropout=0.1,
    )

    epochs = 30
    batch_size = 16
    peak_lr = 3e-4
    min_lr = 3e-5
    weight_decay = 0.1
    warmup_steps = 50

    ds = MPDDataset(ml_dir / "dataset.jsonl", cfg.max_seq_len)
    print(f"Dataset: {len(ds)} sequences")
    loader = DataLoader(ds, batch_size=batch_size, shuffle=True, num_workers=0)

    model = LegoGPT(cfg)
    print(f"Model params: {model.num_params():,}")

    device = torch.device("cpu")
    model.to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=peak_lr, weight_decay=weight_decay, betas=(0.9, 0.95))

    total_steps = epochs * len(loader)
    print(f"Training: {epochs} epochs × {len(loader)} batches = {total_steps} steps")

    save_path = ml_dir / "model.pt"
    log_path = ml_dir / "train.log"
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
            if step % 25 == 0:
                elapsed = time.time() - t0
                print(f"  step {step:4d}/{total_steps}  loss={loss.item():.4f}  lr={lr:.2e}  ({elapsed:.0f}s)")

        avg_loss = ep_loss / max(ep_n, 1)
        print(f"epoch {epoch+1}/{epochs}  avg_loss={avg_loss:.4f}")
        log.append({"epoch": epoch + 1, "avg_loss": avg_loss, "step": step})

        # Save checkpoint every epoch
        torch.save({"model": model.state_dict(), "cfg": cfg.__dict__, "vocab_path": str(ml_dir / "vocab.json"), "epoch": epoch + 1}, save_path)

    log_path.write_text("\n".join(json.dumps(r) for r in log))
    print(f"\nSaved {save_path}")
    print(f"Total time: {time.time() - t0:.0f}s")
    print(f"Final loss: {log[-1]['avg_loss']:.4f}")


if __name__ == "__main__":
    main()
