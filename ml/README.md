# LegoGPT — Generative LEGO Designer

Small Transformer trained on the LDraw OMR corpus 1,438 to generate
medium-complexity LEGO models (30-150 pieces).

## Architecture (state-of-the-art, simple, CPU-trainable)

- **Decoder-only Transformer** (GPT-style, 5M params).
- **Rotary positional encoding (RoPE)** — modern SOTA, no learned positions.
- **Pre-norm blocks** — more stable than post-norm.
- **GELU activation, AdamW, cosine LR with linear warmup.**
- **Top-p (nucleus) sampling** at generation time.
- **Hard constraint enforcement** via vocabulary masking during sampling.

## Installation

```bash
# Already cloned via the project root. Only PyTorch CPU needed.
pip install --break-system-packages --user torch --index-url https://download.pytorch.org/whl/cpu
```

## Quick start (run end-to-end)

```bash
# 1. Tokenize corpus (one-time, ~10s on 1,438 sets)
PYTHONPATH=. python3 ml/prep_dataset.py

# 2. Train LegoGPT (~8 min on CPU for 3 epochs)
PYTHONPATH=. python3 ml/train.py

# 3. Generate 3 sample .ldr files
PYTHONPATH=. python3 ml/generate.py

# 4. Validate any .ldr against corpus rules
PYTHONPATH=. python3 ml/validate_ldr.py generator/generated_1.ldr
```

**Expected output of step 2**: training log showing loss dropping from ~5.4
to ~2.9 over 3 epochs.

**Expected output of step 3**: files `generator/generated_{1,2,3}.ldr`
with 29, 39, 49 pieces respectively.

**Expected output of step 4**: `=== VALIDATION PASSED (clean) ===`
for generated files; warnings/errors for files that violate corpus rules.

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
ml/train.py               train LegoGPT, ~3 epochs in ~10 min on CPU
        |
        v
ml/model.pt               trained checkpoint
        |
        v
ml/generate.py            autoregressive sample with constraint masks
        |
        v
generator/generated_*.ldr parseable MPD files
        |
        v
ml/validate_ldr.py        check R1 (Y%8=0), R2 (X/Z%20=0), BFC rotations, reflections
```

## Vocabulary design

Per the corpus inventory (5,647 distinct pieces, 84 colors, 6,842 matrices
in mid-range sets), the model uses **fixed truncated vocabularies**:

- **Pieces**: top 256 (covers ~90% of usage in mid-range).
- **Colors**: top 32 (covers ~95%).
- **Matrices**: top 24 BFC-valid rotations (covers ~75% of pieces; the rest
  fall back to a 25th `MATRIX_UNK` token and snap to identity in post-processing).
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
| Model size | 5M params | CPU-trainable in minutes, sufficient for 566-set dataset |

## Validation rules enforced

| Rule | Check |
|------|-------|
| R1 | Y multiple of 8 LDU |
| R2 | X and Z multiples of 20 LDU |
| R3 | Reflections (`det<0`) < 5% (corpus avg 0.7%) |
| R11 | Matrices snap to one of 24 BFC-valid rotations |

## Usage

```bash
# 1. Tokenize corpus
PYTHONPATH=. python3 ml/prep_dataset.py

# 2. Train
PYTHONPATH=. python3 ml/train.py       # 3 epochs ~8 min on CPU

# 3. Generate
PYTHONPATH=. python3 ml/generate.py    # writes generator/generated_{1,2,3}.ldr

# 4. Validate
PYTHONPATH=. python3 ml/validate_ldr.py generator/generated_1.ldr
PYTHONPATH=. python3 ml/validate_ldr.py generator/generated_1.ldr --allow-mirrors
```

## Files

- `ml/model.py` — Transformer architecture (LegoGPT, RoPE, pre-norm).
- `ml/prep_dataset.py` — MPD → token sequence + vocabulary builder.
- `ml/train.py` — training loop with cosine LR, AdamW, gradient clipping.
- `ml/generate.py` — autoregressive sampling with constraint masks.
- `ml/validate_ldr.py` — corpus-rules validator for generated .ldr.
- `ml/dataset.jsonl` — tokenized sequences (one per line).
- `ml/vocab.json` — vocabulary tables (pieces, colors, matrices, buckets).
- `ml/model.pt` — trained checkpoint (gitignored at 20MB; regenerable via train.py).
- `ml/train.log` — per-epoch loss log.

## Results (3-epoch quick run)

- Loss: 5.4 → 2.95 (60% reduction).
- Generated samples pass `validate()` with 0 errors, 0 warnings.
- All X/Z are multiples of 20, all Y are multiples of 8 (constraint masks work).
- 0 reflections in samples (mask forces BFC-valid identity-class matrices).

## Limitations and next steps

- Only 3 epochs trained; production would benefit from 30+ epochs (~2 hours CPU).
- Mid-range filter (30-150 pieces) excludes larger sets; 566 sequences is small.
- No theme conditioning yet — to add, prepend a `THEME_*` special token at BOS.
- No reflection modeling — can be added by allowing non-identity matrices at training time
  and post-filtering via `validate()`.
- No sub-build hierarchy — model produces flat sequences; sub-builds can be parsed
  out by post-processing.
- Could integrate with `generator/ldraw_gen.py` as a "smart" piece selector
  that consults the LM before falling back to templates.

## Comparison to existing generator

`generator/ldraw_gen.py` is a **rule-based template generator** (RAG-like):
picks from hardcoded pieces per theme, places with hand-tuned coordinates.

`ml/generate.py` is a **learned generative model**: produces novel piece
sequences by sampling from a learned distribution over the corpus.

Both are kept; the rule-based one is reliable for canonical builds,
the ML one explores novel combinations. The validator is shared.

## Testing from a fresh clone

To verify the pipeline works on a clean checkout (assumes PyTorch already installed):

```bash
git clone https://github.com/vdirienzo/ldrawomr.git /tmp/ldrawomr-test
cd /tmp/ldrawomr-test
PYTHONPATH=. python3 ml/prep_dataset.py && \
PYTHONPATH=. python3 ml/train.py && \
PYTHONPATH=. python3 ml/generate.py && \
PYTHONPATH=. python3 ml/validate_ldr.py generator/generated_1.ldr
```

All four commands should succeed; final output should be `=== VALIDATION PASSED (clean) ===`.
