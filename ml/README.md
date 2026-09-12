# LegoGPT — Generative LEGO Designer

Small Transformer trained on the LDraw OMR corpus 1,438 to generate
medium-complexity LEGO models (30-150 pieces).

## Current model (v3) — 2026-09-12

| | v1 (initial) | v3 (current) |
|---|---|---|
| **Params** | 5.0M | **7.7M** |
| **d_model** | 256 | **320** |
| **n_layers** | 6 | 6 |
| **d_ff** | 1024 | **1280** |
| **Context** | 512 | 512 |
| **Dataset** | 566 sequences | 566 sequences |
| **Epochs** | 3 | **30** |
| **Final loss** | 2.95 | **1.17** |
| **Train time** | 8 min | **86 min** |
| **Validity rate** | 100% (mask-enforced) | **100%** |
| **Unique pieces / 20 samples** | ~50 | **98** |

## Architecture (state-of-the-art, simple, CPU-trainable)

- **Decoder-only Transformer** (GPT-style).
- **Rotary positional encoding (RoPE)** — modern SOTA, no learned positions.
- **Pre-norm blocks** — more stable than post-norm.
- **GELU activation, AdamW (wd=0.1), cosine LR with linear warmup.**
- **Top-p (nucleus) sampling** at generation time.
- **Hard constraint enforcement** via vocabulary masking during sampling.

## Installation

```bash
pip install --break-system-packages --user torch --index-url https://download.pytorch.org/whl/cpu
```

## Quick start (run end-to-end)

```bash
# 1. Tokenize corpus (one-time, ~10s on 1,438 sets → 566 mid-range sequences)
PYTHONPATH=. python3 ml/prep_dataset.py

# 2. Train LegoGPT v3 (~86 min on CPU for 30 epochs, loss 5.27 → 1.17)
PYTHONPATH=. python3 ml/train_v3.py

# 3. Use the trained model (copy v3 over default model.pt, or generate.py auto-detects)
cp ml/model_v3.pt ml/model.pt
PYTHONPATH=. python3 ml/generate.py    # writes generator/generated_{1,2,3}.ldr

# 4. Validate
PYTHONPATH=. python3 ml/validate_ldr.py generator/generated_1.ldr

# 5. (Optional) Benchmark — generate 20 samples, measure validity rate
PYTHONPATH=. python3 ml/benchmark.py
```

**Expected output**:
- Step 2: training log showing loss dropping 5.27 → 1.17 over 30 epochs.
- Step 3: 3 sample .ldr files, each passes validate() cleanly.
- Step 5: validity rate 100%, ~98 unique pieces across 20 samples.

## Pipeline

```
corpus/mpds_*/           (1,438 sets across 8 cohorts, ~534k pieces)
        |
        v
ml/prep_dataset.py        tokenize MPDs into integer sequences
        |
        v
ml/dataset.jsonl          566 sequences (mid-range 30-150 pieces), 343k tokens
ml/vocab.json             256 pieces + 32 colors + 24 matrices + 64 X + 32 Y + 64 Z
        |
        v
ml/train_v3.py            train LegoGPT v3, 30 epochs in 86 min on CPU
        |
        v
ml/model.pt (= v3)        trained checkpoint (30MB, gitignored, regenerable)
        |
        v
ml/generate.py            autoregressive sample with constraint masks
        |
        v
generator/generated_*.ldr parseable MPD files (29/39/49 piezas)
        |
        v
ml/validate_ldr.py        check R1 (Y%8=0), R2 (X/Z%20=0), BFC rotations, reflections
```

## Vocabulary design

Per the corpus inventory (5,647 distinct pieces, 84 colors, 6,842 matrices
in mid-range sets), the model uses **fixed truncated vocabularies**:

- **Pieces**: top 256 (covers ~90% of usage in mid-range).
- **Colors**: top 32 (covers ~95%).
- **Matrices**: top 24 BFC-valid rotations (covers ~75% of pieces).
- **Coordinates**: snap to nearest bucket (top 64 X/Z, top 32 Y by frequency),
  aligned with R2 (X/Z multiples of 20) and R1 (Y multiples of 8).

Each type-1 line emits **6 tokens**: piece, color, matrix, x, y, z.
Special tokens: `BOS`, `EOS`, `STEP`, `NOFILE`, `FILE`, plus UNKs.

## State-of-the-art choices

| Decision | Choice | Rationale |
|----------|--------|-----------|
| BPE vs fixed vocab | Fixed vocab | Domain highly structured; BPE adds complexity for marginal gain |
| Positional encoding | RoPE | Modern SOTA, no learned params, extrapolates better |
| Block norm | Pre-norm | More stable gradients, easier to train deep |
| Sampling | Top-p (nucleus) | Keeps distribution mass, kills tail noise |
| Constraints | Vocabulary mask during sampling | Forces R1/R2 compliance by construction |
| Coordinate quantize | Bucket snap (X±10 LDU tolerance) | Avoids huge coord vocab |
| Model size | 7.7M | Sweet spot for 566 sequences, CPU-trainable in <2h |
| Optimizer | AdamW (wd=0.1, betas=(0.9, 0.95)) | Modern SOTA for Transformers |
| LR schedule | Linear warmup + cosine decay | Standard for Transformers |

## Validation rules enforced

| Rule | Check |
|------|-------|
| R1 | Y multiple of 8 LDU |
| R2 | X and Z multiples of 20 LDU |
| R3 | Reflections (`det<0`) < 5% (corpus avg 0.7%) |
| R11 | Matrices snap to one of 24 BFC-valid rotations |

## Files

### Core pipeline (v3 production)
- `ml/model.py` — Transformer architecture (LegoGPT, RoPE, pre-norm).
- `ml/prep_dataset.py` — MPD → token sequence + vocabulary builder.
- `ml/train_v3.py` — training loop, 30 epochs, 7.7M params.
- `ml/generate.py` — autoregressive sampling with constraint masks.
- `ml/validate_ldr.py` — corpus-rules validator for .ldr files.
- `ml/benchmark.py` — generates 20 samples, reports validity rate.

### Legacy v1 (kept for reference)
- `ml/train.py` — 3-epoch quick trainer (5M params).
- `ml/model_v3.pt` — current trained model (v3, 30 epochs).
- `ml/model.pt` — symlink target (set to v3 by default).

### Data
- `ml/dataset.jsonl` — tokenized sequences (mid-range 30-150 pieces).
- `ml/vocab.json` — vocabulary tables.
- `ml/dataset_v2.jsonl` — v2 dataset (sliding window, 3529 chunks, kept for future use).
- `ml/vocab_v2.json` — v2 vocabulary with theme tokens (kept for future use).
- `ml/train_v3.log` — per-epoch loss log (5.27 → 1.17).
- `ml/benchmark_v3.json` — benchmark results (validity rate, unique pieces).

## Results (30-epoch run, v3)

- **Loss: 5.27 → 1.17** (78% reduction; vs v1's 45% reduction).
- **Validity rate: 100%** (20/20 samples pass validate() with 0 errors).
- **98 unique pieces** used across 20 samples (vs v1's ~50), indicating
  the model is using a broader vocabulary.
- Generated samples use real OMR pieces (`4740.dat`, `3815.dat`, `3673.dat`,
  `3820.dat` = windshield slope, `3062b.dat` = brick 1×2 round, etc.).
- 0 reflections in samples (constraint masks force BFC-valid matrices).

## Limitations and next steps

- No theme conditioning at sampling time yet — would require tokenizing with
  theme at BOS (dataset v2 already supports this; inference path pending).
- 566 sequences is still small; with theme conditioning + 3,529 chunks from
  sliding window (dataset v2), loss could drop further to ~0.8.
- No reflection modeling — constraint masks prevent reflections entirely
  (conservative; loses some thematic variety).
- No sub-build hierarchy — model produces flat sequences.
- Could integrate with `generator/ldraw_gen.py` as a "smart piece picker".

## Comparison to existing generator

`generator/ldraw_gen.py` is a **rule-based template generator** (RAG-like):
picks from hardcoded pieces per theme, places with hand-tuned coordinates.
8 validated demos, 0 errors / 0 warnings.

`ml/generate.py` (LegoGPT v3) is a **learned generative model**: produces novel
piece sequences by sampling from a learned distribution over the corpus.
100% validity, structurally more diverse (98 unique pieces / 20 samples).

Both are kept; the rule-based one is reliable for canonical builds
(looks like what you'd expect — a car, a castle, etc.), the ML one
explores novel combinations (varied but may not be recognizable).

## Testing from a fresh clone

```bash
git clone https://github.com/vdirienzo/ldrawomr.git /tmp/ldraw-test
cd /tmp/ldraw-test
pip install --break-system-packages --user torch --index-url https://download.pytorch.org/whl/cpu
PYTHONPATH=. python3 ml/prep_dataset.py          # ~10s
PYTHONPATH=. timeout 5400 python3 ml/train_v3.py  # 30 epochs, ~86 min
cp ml/model_v3.pt ml/model.pt
PYTHONPATH=. python3 ml/generate.py               # ~10s
PYTHONPATH=. python3 ml/validate_ldr.py generator/generated_1.ldr   # expect: VALIDATION PASSED
PYTHONPATH=. python3 ml/benchmark.py              # expect: 20/20 valid, ~98 unique pieces
cd generator && python3 ldraw_gen.py && cd ..      # expect: All 8 demos generated and validated
```

All checks should pass.
