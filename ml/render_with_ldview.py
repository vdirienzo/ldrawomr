"""
Render LDraw files via LDView CLI (with PIL fallback when unavailable).

When LDView is installed: produces high-quality 3D renders using the
full LDraw Parts Library (corpus/ldraw/parts/) so you see actual
geometry, not bounding boxes.

When LDView is NOT installed: falls back to a PIL-based 2D side view
(same as ml/render_preview.py).

Usage:
    # Render a single file
    PYTHONPATH=. python3 ml/render_with_ldview.py generator/demo_police_car.ldr

    # Render multiple files at standard views
    PYTHONPATH=. python3 ml/render_with_ldview.py generator/demo_*.ldr

    # Generate side-by-side comparison vs rule-based reference
    PYTHONPATH=. python3 ml/render_with_ldview.py \\
        --compare-vs generator/demo_police_car.ldr \\
        generator/generated_1.ldr generator/generated_2.ldr

    # Custom output dir
    PYTHONPATH=. python3 ml/render_with_ldview.py \\
        --out-dir output/renders \\
        generator/demo_*.ldr
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

# Reuse the PIL fallback from render_preview
from ml.render_preview import parse as parse_ldr, render_topdown, render_side


def find_ldview() -> str | None:
    """Locate LDView binary. Returns path or None if not installed."""
    candidates = [
        "ldview", "LDView",
        "/usr/bin/ldview", "/usr/local/bin/ldview",
        "/Applications/LDView.app/Contents/MacOS/LDView",
        "/snap/bin/ldview",
    ]
    for c in candidates:
        found = shutil.which(c) if "/" not in c else (c if Path(c).exists() else None)
        if found:
            return found
    return None


def render_with_ldview(ldr_path: Path, out_png: Path, ldview: str,
                       width: int = 800, height: int = 600,
                       view_angle: str = "0,45,45") -> bool:
    """Render an LDraw file via LDView CLI. Returns True on success."""
    if not Path(ldview).exists():
        return False
    out_png.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        ldview,
        str(ldr_path),
        f"--Save={out_png}",
        "--SaveWidth=" + str(width),
        "--SaveHeight=" + str(height),
        f"--ViewAngle={view_angle}",
        "--DefaultColor=16",  # gray background
        "--HighlightNew=0",
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        return result.returncode == 0 and out_png.exists() and out_png.stat().st_size > 1000
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f"LDView failed for {ldr_path}: {e}", file=sys.stderr)
        return False


def render_fallback(ldr_path: Path, out_png: Path, view: str = "side", scale: int = 30) -> bool:
    """PIL fallback renderer (top-down or side view)."""
    pieces = parse_ldr(ldr_path)
    if not pieces:
        return False
    if view == "top":
        img = render_topdown(pieces, scale=scale)
    else:
        img = render_side(pieces, scale=scale)
    out_png.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_png)
    return True


def render(ldr_path: Path, out_png: Path, ldview: str | None, view: str = "side") -> dict:
    """Render with best available method. Returns metadata."""
    result = {"path": str(ldr_path), "out": str(out_png), "method": "none"}
    if ldview:
        if render_with_ldview(ldr_path, out_png, ldview):
            result["method"] = "ldview"
            return result
        print(f"  [fallback] LDView unavailable for {ldr_path.name}", file=sys.stderr)
    if render_fallback(ldr_path, out_png, view=view):
        result["method"] = f"pil-{view}"
    return result


def make_html_report(renders: list, ref_render: Path | None, out_html: Path) -> None:
    """Generate side-by-side comparison HTML."""
    rows = []
    for r in renders:
        name = Path(r["path"]).stem
        rows.append(f"""
        <tr>
          <td class="name">{name}</td>
          <td><img src="{Path(r['out']).name}" alt="{name}" /></td>
          <td class="method">{r['method']}</td>
        </tr>""")

    ref_section = ""
    if ref_render and ref_render.exists():
        ref_section = f"""
    <h2>Reference (rule-based)</h2>
    <p>{ref_render.name}</p>
    <img src="{ref_render.name}" class="ref" alt="reference" />"""

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>LDraw Renders</title>
<style>
body {{ font-family: system-ui; padding: 20px; background: #1a1a1a; color: #eee; }}
h1 {{ color: #f0c000; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ padding: 8px; border: 1px solid #444; vertical-align: top; }}
th {{ background: #2a2a2a; text-align: left; }}
img {{ max-width: 400px; height: auto; display: block; }}
.name {{ font-family: monospace; }}
.method {{ font-size: 0.85em; color: #888; }}
.ref {{ max-width: 600px; margin: 20px 0; }}
.caption {{ color: #aaa; font-size: 0.9em; }}
</style></head><body>
<h1>LegoGPT — Generated Models Rendered</h1>
<p class="caption">Side-by-side: ML-generated samples vs rule-based reference.</p>

<table>
<thead><tr><th>Model</th><th>Render</th><th>Method</th></tr></thead>
<tbody>
{''.join(rows)}
</tbody>
</table>
{ref_section}
</body></html>"""

    out_html.parent.mkdir(parents=True, exist_ok=True)
    out_html.write_text(html)
    print(f"Report: {out_html}")


def pixel_diff(render_a: Path, render_b: Path, out_png: Path) -> float | None:
    """Return 0..1 similarity between two renders (1 = identical). None if not available."""
    try:
        from PIL import Image, ImageChops
    except ImportError:
        return None
    if not render_a.exists() or not render_b.exists():
        return None
    a = Image.open(render_a).convert("RGB")
    b = Image.open(render_b).convert("RGB").resize(a.size)
    diff = ImageChops.difference(a, b)
    # Mean absolute difference
    pixels = list(diff.getdata())
    if not pixels:
        return None
    total = sum(sum(p) for p in pixels)
    avg = total / (len(pixels) * 3 * 255)
    similarity = 1.0 - avg
    # Save diff visualization
    out_png.parent.mkdir(parents=True, exist_ok=True)
    diff.save(out_png)
    return similarity


def main():
    parser = argparse.ArgumentParser(description="Render LDraw files via LDView (with PIL fallback)")
    parser.add_argument("files", nargs="+", type=Path, help=".ldr files to render")
    parser.add_argument("--out-dir", type=Path, default=Path("output/renders"),
                        help="output directory for PNG renders")
    parser.add_argument("--view", choices=["side", "top"], default="side",
                        help="view for fallback renderer")
    parser.add_argument("--compare-vs", type=Path, default=None,
                        help="reference .ldr to render for side-by-side")
    parser.add_argument("--report", type=Path, default=None,
                        help="output HTML report path")
    parser.add_argument("--diff", action="store_true",
                        help="compute pixel diff against reference render")
    args = parser.parse_args()

    out_dir = args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    ldview = find_ldview()
    if ldview:
        print(f"Using LDView: {ldview}")
    else:
        print("LDView not found — using PIL fallback (basic 2D view).")
        print("Install LDView for high-quality 3D rendering: https://ldview.sourceforge.io/")

    renders = []
    for ldr in args.files:
        if not ldr.exists():
            print(f"  skip: {ldr} (not found)")
            continue
        out_png = out_dir / f"{ldr.stem}.png"
        meta = render(ldr, out_png, ldview, view=args.view)
        print(f"  {ldr.name} -> {out_png.name}  [{meta['method']}]")
        renders.append(meta)

    # Render reference
    ref_render_path = None
    if args.compare_vs and args.compare_vs.exists():
        ref_render_path = out_dir / f"ref_{args.compare_vs.stem}.png"
        meta = render(args.compare_vs, ref_render_path, ldview, view=args.view)
        print(f"  ref {args.compare_vs.name} -> {ref_render_path.name}  [{meta['method']}]")
        renders.insert(0, {"path": str(args.compare_vs), "out": str(ref_render_path), "method": meta["method"]})

    # Pixel diff
    if args.diff and ref_render_path:
        for r in renders[1:]:
            diff_path = out_dir / f"diff_{Path(r['path']).stem}_vs_ref.png"
            sim = pixel_diff(Path(r["out"]), ref_render_path, diff_path)
            if sim is not None:
                print(f"  similarity({Path(r['path']).stem} vs ref) = {sim:.3f}")
                print(f"    diff: {diff_path}")

    # HTML report
    if args.report is None:
        args.report = out_dir / "index.html"
    make_html_report(renders, ref_render_path, args.report)


if __name__ == "__main__":
    main()
