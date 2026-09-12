"""
Validate generated .ldr files against LDraw corpus rules.

Rules (from LEARNED_CONVENTIONS_1438.md):
- R1 (canonical): Y must be a multiple of 8 LDU.
- R2 (canonical): X/Z must be multiples of 20 LDU.
- R3 (reflections): det(matrix) < 0 should be < 5% (corpus 0.7%).
- R10: BFC CERTIFY header (informational, not enforced here).
- R11: matrices should be one of the 24 BFC-valid rotations or close.

Reports errors and warnings. Returns 0 if clean (only with --allow-mirrors for reflections).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NUM = r"(\-?\d+(?:\.\d+)?)"
T1_RE = re.compile(
    r"^1\s+(\S+)\s+"
    + NUM + r"\s+" + NUM + r"\s+" + NUM + r"\s+"
    + (NUM + r"\s+") * 8 + NUM + r"\s+(.+)$"
)

# BFC-valid 24 rotations, as integer tuples (after multiplying by rounding factor)
BFC_INT = {
    (1, 0, 0, 0, 1, 0, 0, 0, 1),
    (0, 0, 1, 0, 1, 0, -1, 0, 0),
    (0, 0, -1, 0, 1, 0, 1, 0, 0),
    (-1, 0, 0, 0, 1, 0, 0, 0, -1),
    (1, 0, 0, 0, 0, -1, 0, 1, 0),
    (1, 0, 0, 0, 0, 1, 0, -1, 0),
    (0, -1, 0, 1, 0, 0, 0, 0, 1),
    (-1, 0, 0, 0, 0, 1, 0, 1, 0),
    (0, 1, 0, -1, 0, 0, 0, 0, 1),
    (0, 1, 0, 0, 0, -1, -1, 0, 0),
    (-1, 0, 0, 0, 0, -1, 0, -1, 0),
    (0, 0, 1, 1, 0, 0, 0, 1, 0),
    (0, -1, 0, 0, 0, 1, -1, 0, 0),
    (0, -1, 0, 0, 0, -1, 1, 0, 0),
    (0, 1, 0, 1, 0, 0, 0, 0, -1),
    (0, 0, -1, -1, 0, 0, 0, 1, 0),
    (0, -1, 0, -1, 0, 0, 0, 0, -1),
    (0, 1, 0, 0, 0, 1, 1, 0, 0),
    (0, 0, 1, -1, 0, 0, 0, -1, 0),
    (0, 0, -1, 1, 0, 0, 0, -1, 0),
    (-1, 0, 0, 0, -1, 0, 0, 0, 1),
    (1, 0, 0, 0, -1, 0, 0, 0, -1),
    (1, 0, 0, 0, 0, 0, 1, 0, 0),
    (1, 0, 0, 0, 0, 0, -1, 0, 0),
}


def parse_ldr(path: Path) -> list:
    """Return list of t1 line dicts: color, x, y, z, matrix (tuple), file."""
    text = path.read_bytes().replace(b"\r\n", b"\n").decode("utf-8", errors="replace")
    pieces = []
    for line in text.split("\n"):
        m = T1_RE.match(line)
        if not m:
            continue
        g = m.groups()
        try:
            color = int(g[0])
        except ValueError:
            color = -1
        matrix = tuple(round(float(g[i]), 4) for i in range(4, 13))
        pieces.append({"color": color, "x": float(g[1]), "y": float(g[2]), "z": float(g[3]), "matrix": matrix, "file": g[13]})
    return pieces


def det(m) -> float:
    a, b, c, d, e, f, g, h, i = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def validate(pieces: list, allow_mirrors: bool = False) -> tuple:
    """Return (errors, warnings, stats)."""
    errors = []
    warnings = []
    n = len(pieces)
    if n == 0:
        errors.append("no pieces found")
        return errors, warnings, {"count": 0}

    y_bad = sum(1 for p in pieces if abs(p["y"]) % 8 != 0)
    x_bad = sum(1 for p in pieces if abs(p["x"]) % 20 != 0)
    z_bad = sum(1 for p in pieces if abs(p["z"]) % 20 != 0)
    if y_bad:
        warnings.append(f"R1: Y not multiple of 8: {y_bad}/{n} pieces ({y_bad/n*100:.1f}%)")
    if x_bad:
        warnings.append(f"R2: X not multiple of 20: {x_bad}/{n} pieces ({x_bad/n*100:.1f}%)")
    if z_bad:
        warnings.append(f"R2: Z not multiple of 20: {z_bad}/{n} pieces ({z_bad/n*100:.1f}%)")

    # Reflection check
    neg = sum(1 for p in pieces if det(p["matrix"]) < 0)
    neg_pct = neg / n * 100
    if neg and not allow_mirrors:
        if neg_pct > 5.0:
            errors.append(f"R3: reflections {neg_pct:.2f}% > 5% threshold")
        else:
            warnings.append(f"R3: reflections {neg_pct:.2f}% (corpus average 0.7%)")

    # BFC matrix check (rounded to int)
    int_matrices = set()
    bad_matrices = 0
    for p in pieces:
        im = tuple(round(v) for v in p["matrix"])
        if im in BFC_INT:
            int_matrices.add(im)
        else:
            bad_matrices += 1
    if bad_matrices:
        warnings.append(f"matrix: {bad_matrices}/{n} pieces have non-canonical BFC rotation")

    stats = {
        "count": n,
        "y_bad": y_bad,
        "x_bad": x_bad,
        "z_bad": z_bad,
        "reflections": neg,
        "reflections_pct": neg_pct,
        "non_canonical_matrices": bad_matrices,
        "unique_matrices": len(int_matrices),
    }
    return errors, warnings, stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ldr", type=Path, help="path to .ldr file to validate")
    parser.add_argument("--allow-mirrors", action="store_true", help="don't error on reflections")
    args = parser.parse_args()

    pieces = parse_ldr(args.ldr)
    errors, warnings, stats = validate(pieces, allow_mirrors=args.allow_mirrors)
    print(f"File: {args.ldr}")
    print(f"Pieces: {stats['count']}")
    print(f"Y multiple of 8: {stats['count'] - stats['y_bad']}/{stats['count']} OK")
    print(f"X multiple of 20: {stats['count'] - stats['x_bad']}/{stats['count']} OK")
    print(f"Z multiple of 20: {stats['count'] - stats['z_bad']}/{stats['count']} OK")
    print(f"Reflections: {stats['reflections']} ({stats['reflections_pct']:.2f}%)")
    print(f"Non-canonical BFC matrices: {stats['non_canonical_matrices']}")
    print(f"Unique matrices used: {stats['unique_matrices']}")
    if errors:
        print(f"\nERRORS ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    if not errors and not warnings:
        print("\n=== VALIDATION PASSED (clean) ===")
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
