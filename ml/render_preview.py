"""
Quick isometric-like top-down renderer for .ldr files.

Renders a top-down view (Z=up on screen, X=right) showing X/Z positions
of all pieces. Each piece is a small colored square.

Colors map LDraw color codes to approximate hex. Unknown colors = gray.

Not a full renderer; just enough to visualize layout and validate structure.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw

# Subset of LDraw colors (LDConfig.ldr color code → RGB)
COLORS = {
    0: (0, 0, 0),         # Black
    1: (0, 75, 165),      # Blue
    2: (0, 138, 48),      # Green
    3: (0, 145, 158),     # Dark turquoise
    4: (175, 30, 35),     # Red
    5: (220, 110, 145),   # Dark pink
    6: (102, 64, 32),     # Brown
    7: (155, 155, 155),   # Light grey
    8: (95, 95, 95),      # Dark grey
    9: (110, 160, 220),   # Light blue
    10: (170, 220, 35),   # Bright green
    11: (45, 195, 215),   # Light turquoise
    12: (245, 130, 110),  # Salmon
    13: (255, 175, 215),  # Pink
    14: (245, 220, 65),   # Yellow
    15: (245, 245, 245),  # White
    19: (210, 170, 100),  # Tan
    25: (245, 145, 30),   # Orange
    27: (175, 220, 30),   # Lime
    28: (130, 90, 50),    # Dark tan
    36: (220, 50, 50),    # Trans red
    47: (210, 230, 255),  # Trans clear / pale blue
    70: (155, 95, 50),    # Reddish brown
    71: (175, 185, 195),  # Light bluish grey
    72: (110, 125, 140),  # Dark bluish grey
    272: (35, 65, 145),   # Dark blue (police)
    326: (175, 200, 30),  # Yellowish green
    320: (180, 95, 30),   # Dark orange / reddish brown
}

NUM = r"(\-?\d+(?:\.\d+)?)"
T1_RE = re.compile(
    r"^1\s+(\S+)\s+"
    + NUM + r"\s+" + NUM + r"\s+" + NUM + r"\s+"
    + (NUM + r"\s+") * 8 + NUM + r"\s+(.+)$"
)


def parse(path):
    pieces = []
    for line in Path(path).read_text().split("\n"):
        m = T1_RE.match(line)
        if not m:
            continue
        g = m.groups()
        try:
            color = int(g[0])
        except ValueError:
            color = -1
        try:
            pieces.append({"color": color, "x": float(g[1]), "y": float(g[2]), "z": float(g[3]), "file": g[13]})
        except ValueError:
            continue
    return pieces


def render_topdown(pieces, scale=12, padding=30):
    """Render top-down view (X→right, Z→up on screen)."""
    if not pieces:
        return Image.new("RGB", (100, 100), "white")
    xs = [p["x"] for p in pieces]
    zs = [p["z"] for p in pieces]
    min_x, max_x = min(xs), max(xs)
    min_z, max_z = min(zs), max(zs)
    w = int((max_x - min_x) * scale) + 2 * padding
    h = int((max_z - min_z) * scale) + 2 * padding
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    for p in pieces:
        cx = int((p["x"] - min_x) * scale) + padding
        cz = int((p["z"] - min_z) * scale) + padding
        color = COLORS.get(p["color"], (128, 128, 128))
        # Draw a circle for each piece (1 stud = scale pixels diameter)
        r = scale // 2
        draw.ellipse([cx - r, cz - r, cx + r, cz + r], fill=color, outline="black")
    return img


def render_side(pieces, scale=12, padding=30):
    """Render side view (X→right, Y→up on screen, Y negative = up)."""
    if not pieces:
        return Image.new("RGB", (100, 100), "white")
    xs = [p["x"] for p in pieces]
    ys = [p["y"] for p in pieces]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    # Y is inverted (negative Y goes up)
    w = int((max_x - min_x) * scale) + 2 * padding
    h = int((max_y - min_y) * scale) + 2 * padding
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    for p in pieces:
        cx = int((p["x"] - min_x) * scale) + padding
        # Flip Y axis: most negative Y goes at TOP of image
        cy = int((-p["y"] - -max_y) * scale) + padding
        color = COLORS.get(p["color"], (128, 128, 128))
        r = scale // 2
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=color, outline="black")
    return img


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ldr", type=Path)
    parser.add_argument("--out", type=Path, default=None, help="output PNG path")
    parser.add_argument("--view", choices=["top", "side", "both"], default="both")
    parser.add_argument("--scale", type=int, default=12)
    args = parser.parse_args()

    pieces = parse(args.ldr)
    if args.view in ("top", "both"):
        img = render_topdown(pieces, scale=args.scale)
        out = args.out or args.ldr.with_suffix(".top.png")
        img.save(out)
        print(f"Saved top-down view: {out} ({img.size[0]}x{img.size[1]})")
    if args.view in ("side", "both"):
        img = render_side(pieces, scale=args.scale)
        out = args.out or args.ldr.with_suffix(".side.png")
        # Avoid overwriting top
        if args.view == "both":
            out = args.ldr.with_suffix(".side.png")
        img.save(out)
        print(f"Saved side view: {out} ({img.size[0]}x{img.size[1]})")


if __name__ == "__main__":
    main()
