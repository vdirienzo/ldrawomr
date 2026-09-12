# LDView Integration — Plan & Status

**Goal**: Render `.ldr` files with LDView for visual validation of ML-generated models.

## Status (2026-09-12)

- [x] `ml/render_with_ldview.py` implemented
- [x] PIL fallback works (verified on this machine)
- [ ] LDView binary not yet installed in this environment
- [ ] Side-by-side HTML report generated and tested
- [x] Pixel-diff against reference render computed
- [ ] Add to dashboard.html integration (next session)

## How it works

```
.ldr file
   |
   v
ml/render_with_ldview.py
   |
   +-- detect LDView --yes--> subprocess ldview --Save=foo.png input.ldr
   |                          (high-quality 3D render using corpus/ldraw/parts/)
   |
   +-- LDView missing -----> ml/render_preview.py fallback
                              (PIL 2D dots, basic but always works)
   |
   v
output/renders/<name>.png
output/renders/diff_<name>_vs_ref.png  (pixel-wise similarity)
output/renders/index.html              (side-by-side HTML report)
```

## Usage

### Basic render

```bash
# Single file
PYTHONPATH=. python3 ml/render_with_ldview.py generator/demo_police_car.ldr

# Multiple files
PYTHONPATH=. python3 ml/render_with_ldview.py generator/demo_*.ldr
```

### Comparison vs reference

```bash
PYTHONPATH=. python3 ml/render_with_ldview.py \
  --compare-vs generator/demo_police_car.ldr \
  --diff \
  --report output/renders/index.html \
  generator/generated_1.ldr \
  generator/generated_2.ldr \
  generator/generated_3.ldr
```

Outputs:
- `output/renders/generated_1.png` (and 2, 3)
- `output/renders/ref_demo_police_car.png`
- `output/renders/diff_generated_X_vs_ref.png` (pixel-wise similarity)
- `output/renders/index.html` (HTML side-by-side)

### Custom output dir

```bash
PYTHONPATH=. python3 ml/render_with_ldview.py \
  --out-dir output/batch1 \
  generator/demo_*.ldr
```

## LDView install (for next session)

To enable high-quality 3D rendering:

```bash
# Ubuntu/Debian
sudo apt install ldview

# macOS (Homebrew)
brew install --cask ldview

# From source
# https://ldview.sourceforge.io/Downloads.html
```

LDView uses `corpus/ldraw/parts/` (526 MB mirror we already have) to resolve
geometry. Without LDView installed, the script falls back to PIL 2D dot
rendering (current behavior).

## Why we need this

The user previously saw ML-generated renders that looked like "junk drawers"
(tan brick piles, scattered Technic pieces). Without LDView rendering, we
can't visually inspect what the model produces. V1/V3/V4 validations only
check R1/R2/R3 rules (coordinate multiples, BFC matrices, reflections) —
they don't check "does this look like a car?".

LDView integration enables:
- **Visual diff** between rule-based reference (known good) and ML output
- **Qualitative evaluation** by humans (just open the HTML report)
- **Future automated scoring** via vision models or learned metrics

## Next session work

### After installing LDView

```bash
# Verify LDView is found
ldview --version
# Should print version info

# Re-run renders with high quality
PYTHONPATH=. python3 ml/render_with_ldview.py \
  --out-dir output/renders \
  --compare-vs generator/demo_police_car.ldr \
  --diff \
  --report output/renders/index.html \
  generator/generated_1.ldr \
  generator/generated_2.ldr \
  generator/generated_3.ldr

# Look at the renders
xdg-open output/renders/index.html  # Linux
open output/renders/index.html       # macOS
```

### After v5 training completes

```bash
# Generate town-themed samples
PYTHONPATH=. python3 ml/generate.py --theme THEME_TOWN_CLASSIC

# Render and compare
PYTHONPATH=. python3 ml/render_with_ldview.py \
  --compare-vs generator/demo_town.ldr \
  --diff \
  --report output/renders/v5_town.html \
  generator/generated_1.ldr generator/generated_2.ldr generator/generated_3.ldr
```

### Optional: integrate with dashboard

Add link from `output/dashboard.html` to `output/renders/index.html` for
visual exploration of generated samples.

## Files

- `ml/render_with_ldview.py` — main script (LDView + PIL fallback)
- `ml/render_preview.py` — basic PIL 2D renderer (existing)
- `output/renders/index.html` — generated HTML report
- `output/renders/<name>.png` — rendered PNGs
- `output/renders/diff_<name>_vs_ref.png` — pixel diff visualization

## Limitations

1. **PIL fallback** shows pieces as colored circles, not actual geometry.
2. **Pixel diff** is a coarse metric — two visually different renders can
   have high similarity (e.g., a 90° rotated version).
3. **LDView must be installed** for the high-quality path. Without it, we
   only see "did the model place pieces in valid positions" not "does
   it look like the requested theme".
4. **No structural validation** — the diff doesn't tell us if the bricks
   are physically connected. That's a separate problem (would require
   parsing geometry from parts/).
