# LDView Integration — Plan & Status

**Goal**: Render `.ldr` files with LDView for visual validation of ML-generated models.

## Status (2026-09-12)

- [x] `ml/render_with_ldview.py` implemented
- [x] PIL fallback works (verified)
- [x] **LDView Flatpak installed** (io.github.tcobbs.LDView 4.7)
- [x] Auto-detects Flatpak install via `find_ldview()`
- [ ] LDView headless render NOT WORKING in this environment (Qt platform issues)
- [x] Side-by-side HTML report generated and tested
- [x] Pixel-diff against reference render computed

## Flatpak install

```bash
# LDView is NOT in apt (Error: Unable to locate package ldview).
# It IS in flathub. Install via:
flatpak install --user --assumeyes flathub io.github.tcobbs.LDView

# Binary found at:
~/.local/share/flatpak/app/io.github.tcobbs.LDView/x86_64/stable/active/files/bin/LDView
```

LDView bundles its own LDraw library at `share/ldraw/parts/` (17,503 parts).

## Known issue: headless rendering

LDView needs a Qt display. In headless environments (no X11 server, no
Wayland) it fails with:
```
Failed to create wl_display (No such file or directory)
qt.qpa.plugin: Could not load the Qt platform plugin "wayland"
```

Workarounds attempted:
- `DISPLAY=:0` (no real X server, just socket)
- `QT_QPA_PLATFORM=xcb` (xcb plugin not in flatpak runtime)
- `QT_QPA_PLATFORM=offscreen` (LDView's save dialog needs setParent, not supported)
- `flatpak run --filesystem=...` (sandbox blocks host filesystem)

**Conclusion**: LDView from flatpak won't render headless in this env.
The PIL fallback (`ml/render_preview.py`) is the active path.

## When LDView will work

LDView will produce real 3D renders when:
1. You're on a system with a real X11/Wayland display (your local PC, not this sandbox)
2. The user has confirmed `LDView` is installed locally with sudo/apt/brew
3. The `find_ldview()` will pick it up automatically

## How it works

```
.ldr file
   |
   v
ml/render_with_ldview.py
   |
   +-- detect LDView --yes--> subprocess LDView --Save=foo.png input.ldr
   |                          (high-quality 3D render using LDraw parts)
   |
   +-- LDView missing/headless -> ml/render_preview.py fallback
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

### On user's local PC (where LDView actually works)

```bash
# Verify LDView is found
ldview --version

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
# Resume v5 training
PYTHONPATH=. python3 ml/train_v5.py

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
- `ml/render_preview.py` — basic PIL 2D renderer (existing, the active fallback)
- `output/renders/index.html` — generated HTML report
- `output/renders/<name>.png` — rendered PNGs
- `output/renders/diff_<name>_vs_ref.png` — pixel diff visualization

## Limitations

1. **LDView headless render NOT WORKING** in this sandbox environment.
   PIL fallback is the active path.
2. **PIL fallback** shows pieces as colored circles, not actual geometry.
3. **Pixel diff** is a coarse metric — two visually different renders can
   have high similarity (e.g., a 90° rotated version).
4. **LDView must be installed** for the high-quality path. Without it, we
   only see "did the model place pieces in valid positions" not "does
   it look like the requested theme".
5. **No structural validation** — the diff doesn't tell us if the bricks
   are physically connected. That's a separate problem (would require
   parsing geometry from parts/).
