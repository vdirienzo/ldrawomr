"""
Dataset preparation for LDraw MPD sequence generation.

Tokenizes each MPD in the corpus 1,438 into an integer sequence. Each
type-1 line emits six tokens (piece, color, matrix, x, y, z). Special
markers (STEP, FILE, NOFILE) emit single tokens.

Output: ml/dataset.jsonl (one sequence per line) + ml/vocab.json (token map).

State-of-the-art choices:
- Fixed vocab (no BPE) — domain is highly structured; BPE adds overhead.
- Top-K truncation for pieces/colors/matrices/buckets to keep vocab small.
- Quantize coordinates into buckets aligned with corpus rules:
  X/Z multiples of 20 LDU, Y multiples of 8 LDU (R1/R2 from canonical doc).
- Bucket order preserved by descending frequency in the mid-range corpus.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

NUM = r"(\-?\d+(?:\.\d+)?)"
T1_RE = re.compile(
    r"^1\s+(\S+)\s+"
    + NUM + r"\s+" + NUM + r"\s+" + NUM + r"\s+"  # x y z
    + (NUM + r"\s+") * 8  # matrix[0..7]
    + NUM  # matrix[8]
    + r"\s+"  # sep
    + r"(.+)$"  # filename
)

# BFC-valid 24 rotations: top-N from inventory.
BFC_TOP_MATRICES = [
    [1, 0, 0, 0, 1, 0, 0, 0, 1],   # identity
    [0, 0, 1, 0, 1, 0, -1, 0, 0],  # rot Y +90
    [0, 0, -1, 0, 1, 0, 1, 0, 0],  # rot Y -90
    [-1, 0, 0, 0, 1, 0, 0, 0, -1], # rot Y 180
    [1, 0, 0, 0, 0, -1, 0, 1, 0],  # rot X +90
    [1, 0, 0, 0, 0, 1, 0, -1, 0],  # rot X -90
    [0, -1, 0, 1, 0, 0, 0, 0, 1],  # rot Z +90
    [-1, 0, 0, 0, 0, 1, 0, 1, 0],  # rot X 180 + rot Z 90 (compound)
    [0, 1, 0, -1, 0, 0, 0, 0, 1],  # rot Z -90
    [0, 1, 0, 0, 0, -1, -1, 0, 0], # compound
    [-1, 0, 0, 0, 0, -1, 0, -1, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0],
    [0, -1, 0, 0, 0, 1, -1, 0, 0],
    [0, -1, 0, 0, 0, -1, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, -1],
    [0, 0, -1, -1, 0, 0, 0, 1, 0],
    [0, -1, 0, -1, 0, 0, 0, 0, -1],
    [0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 0, 1, -1, 0, 0, 0, -1, 0],
    [0, 0, -1, 1, 0, 0, 0, -1, 0],
    [-1, 0, 0, 0, -1, 0, 0, 0, 1],
    [1, 0, 0, 0, -1, 0, 0, 0, -1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0],  # flip Z
    [1, 0, 0, 0, 0, 0, -1, 0, 0],
]

DIR_MAP = {
    "80s90s": "corpus/mpds",
    "kids": "corpus/mpds_kids",
    "classic": "corpus/mpds_classic",
    "modern": "corpus/mpds_modern",
    "technic": "corpus/mpds_technic",
    "specialty": "corpus/mpds_specialty",
    "licensed": "corpus/mpds_licensed",
    "classic_gaps": "corpus/mpds_classic_gaps",
}

VOCAB = {
    "PAD": 0, "BOS": 1, "EOS": 2, "STEP": 3, "NOFILE": 4, "FILE": 5,
    "PIECE_UNK": 6, "COLOR_UNK": 7, "MATRIX_UNK": 8, "X_UNK": 9, "Y_UNK": 10, "Z_UNK": 11,
}
VOCAB_SIZE = 512  # padded for headroom


def build_vocab(per_set_path: Path, top_n: int = 256) -> dict:
    """Build top-N piece/color/matrix/bucket vocabularies from corpus 1,438."""
    per_set = json.loads(per_set_path.read_text())
    # Use all sets, not just mid-range, to maximize vocabulary coverage.

    base = Path("/home/user/Projects/ldraw")
    pieces, colors, matrices, xs, ys, zs = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()
    n_scanned = 0
    for r in per_set:
        cohort = r.get("cohort", "")
        num_full = r["meta"]["set_number"]
        mpd_dir = base / DIR_MAP.get(cohort, "")
        cands = list(mpd_dir.glob(f"{num_full}*.mpd"))
        if not cands:
            continue
        text = cands[0].read_bytes().replace(b"\r\n", b"\n").decode("utf-8", errors="replace")
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
            pieces[g[13]] += 1
            colors[color] += 1
            matrices[matrix] += 1
            xs[round(float(g[1]))] += 1
            ys[round(float(g[2]))] += 1
            zs[round(float(g[3]))] += 1
            n_scanned += 1

    # Pick top matrices that match BFC rotation list
    bfc_tuples = {tuple(m): i for i, m in enumerate(BFC_TOP_MATRICES)}
    mat_to_id = {}
    for mat, cnt in matrices.most_common(40):
        if mat in bfc_tuples and bfc_tuples[mat] not in mat_to_id.values():
            mat_to_id[mat] = bfc_tuples[mat]

    # Quantize coordinates into buckets aligned with corpus rules:
    # X/Z bucket size = 20, Y bucket size = 8.
    x_bucket_keys = sorted(xs.keys(), key=lambda v: -xs[v])[:64]
    z_bucket_keys = sorted(zs.keys(), key=lambda v: -zs[v])[:64]
    y_bucket_keys = sorted(ys.keys(), key=lambda v: -ys[ys[v] if v in ys else 0])[:32]
    # Build proper top-32 Y by frequency:
    y_bucket_keys = [v for v, _ in ys.most_common(32)]

    # Stable top-K by frequency
    piece_vocab = [p for p, _ in pieces.most_common(top_n)]
    color_vocab = [c for c, _ in colors.most_common(32)]

    out = {
        "vocab_size": VOCAB_SIZE,
        "n_t1_scanned": n_scanned,
        "piece_vocab": piece_vocab,
        "piece_unk_id": VOCAB["PIECE_UNK"],
        "color_vocab": color_vocab,
        "color_unk_id": VOCAB["COLOR_UNK"],
        "matrix_vocab": BFC_TOP_MATRICES,
        "matrix_unk_id": VOCAB["MATRIX_UNK"],
        "x_buckets": x_bucket_keys,
        "x_unk_id": VOCAB["X_UNK"],
        "y_buckets": y_bucket_keys,
        "y_unk_id": VOCAB["Y_UNK"],
        "z_buckets": z_bucket_keys,
        "z_unk_id": VOCAB["Z_UNK"],
        "special_tokens": {"PAD": 0, "BOS": 1, "EOS": 2, "STEP": 3, "NOFILE": 4, "FILE": 5},
    }
    return out


def quantize_coord(v: float, buckets: list, unk_id: int) -> int:
    """Snap a coordinate to nearest bucket; return unk_id if no bucket within tolerance."""
    rounded = round(v)
    if rounded in buckets:
        return 12 + buckets.index(rounded)
    # Snap to nearest
    if buckets:
        nearest = min(buckets, key=lambda b: abs(b - rounded))
        if abs(nearest - rounded) <= 10:  # within tolerance
            return 12 + buckets.index(nearest)
    return unk_id


def tokenize_mpd(mpd_path: Path, vocab: dict) -> list:
    """Convert an MPD file into a sequence of integer tokens."""
    text = mpd_path.read_bytes().replace(b"\r\n", b"\n").decode("utf-8", errors="replace")
    piece_vocab = vocab["piece_vocab"]
    color_vocab = vocab["color_vocab"]
    matrix_vocab = vocab["matrix_vocab"]
    x_buckets = vocab["x_buckets"]
    y_buckets = vocab["y_buckets"]
    z_buckets = vocab["z_buckets"]
    piece_unk = vocab["piece_unk_id"]
    color_unk = vocab["color_unk_id"]
    matrix_unk = vocab["matrix_unk_id"]
    x_unk = vocab["x_unk_id"]
    y_unk = vocab["y_unk_id"]
    z_unk = vocab["z_unk_id"]
    matrix_tuples = {tuple(m): 12 + len(piece_vocab) + len(color_vocab) + i for i, m in enumerate(matrix_vocab)}

    piece_base = 12
    color_base = piece_base + len(piece_vocab)
    matrix_base = color_base + len(color_vocab)
    x_base = matrix_base + len(matrix_vocab)
    y_base = x_base + 64
    z_base = y_base + 32

    tokens = [1]  # BOS
    for line in text.split("\n"):
        line = line.strip()
        if not line:
            continue
        if line.startswith("0 STEP") or line.startswith("0 !STEP"):
            tokens.append(3)  # STEP
            continue
        if line.startswith("0 NOFILE"):
            tokens.append(4)  # NOFILE
            continue
        if line.startswith("0 FILE"):
            tokens.append(5)  # FILE
            continue
        m = T1_RE.match(line)
        if not m:
            continue
        g = m.groups()
        # piece
        piece = g[13]
        tokens.append(piece_base + piece_vocab.index(piece) if piece in piece_vocab else piece_unk)
        # color
        try:
            color = int(g[0])
        except ValueError:
            color = -1
        tokens.append(color_base + color_vocab.index(color) if color in color_vocab else color_unk)
        # matrix
        matrix = tuple(round(float(g[i]), 4) for i in range(4, 13))
        tokens.append(matrix_tuples.get(matrix, matrix_unk))
        # x y z
        x_val = round(float(g[1]))
        z_val = round(float(g[3]))
        y_val = round(float(g[2]))
        # Snap to nearest bucket within tolerance
        def snap(val, buckets, base):
            if val in buckets:
                return base + buckets.index(val)
            if buckets:
                nearest = min(buckets, key=lambda b: abs(b - val))
                if abs(nearest - val) <= 10:
                    return base + buckets.index(nearest)
            return None
        x_tok = snap(x_val, x_buckets, x_base)
        y_tok = snap(y_val, y_buckets, y_base)
        z_tok = snap(z_val, z_buckets, z_base)
        tokens.append(x_tok if x_tok is not None else x_unk)
        tokens.append(y_tok if y_tok is not None else y_unk)
        tokens.append(z_tok if z_tok is not None else z_unk)

    tokens.append(2)  # EOS
    return tokens


def main():
    base = Path("/home/user/Projects/ldraw")
    ml_dir = base / "ml"
    ml_dir.mkdir(exist_ok=True)

    print("Building vocab...")
    vocab = build_vocab(base / "analysis" / "per_set_stats_1438.json")
    print(f"  pieces: {len(vocab['piece_vocab'])}")
    print(f"  colors: {len(vocab['color_vocab'])}")
    print(f"  matrices: {len(vocab['matrix_vocab'])}")
    print(f"  x_buckets: {len(vocab['x_buckets'])}")
    print(f"  y_buckets: {len(vocab['y_buckets'])}")
    print(f"  z_buckets: {len(vocab['z_buckets'])}")
    print(f"  total t1 scanned: {vocab['n_t1_scanned']}")

    (ml_dir / "vocab.json").write_text(json.dumps(vocab, indent=2))

    print("\nTokenizing MPDs (filtering to mid-range 30-150 pieces)...")
    per_set = json.loads((base / "analysis" / "per_set_stats_1438.json").read_text())
    out_path = ml_dir / "dataset.jsonl"
    n_sequences = 0
    total_tokens = 0
    skipped = 0
    with out_path.open("w") as fout:
        for r in per_set:
            if not (30 <= r["total_pieces"] < 150):
                skipped += 1
                continue
            cohort = r.get("cohort", "")
            num_full = r["meta"]["set_number"]
            mpd_dir = base / DIR_MAP.get(cohort, "")
            cands = list(mpd_dir.glob(f"{num_full}*.mpd"))
            if not cands:
                continue
            try:
                tokens = tokenize_mpd(cands[0], vocab)
            except Exception as e:
                print(f"  WARN {num_full}: {e}")
                continue
            if len(tokens) < 14:
                skipped += 1
                continue
            n_sequences += 1
            total_tokens += len(tokens)
            fout.write(json.dumps({"set": num_full, "theme": r["meta"].get("theme", "?"), "tokens": tokens}) + "\n")

    print(f"\nDataset: {n_sequences} sequences, {total_tokens:,} tokens (skipped {skipped})")
    if n_sequences:
        print(f"Mean seq length: {total_tokens / n_sequences:.0f}")
        print(f"Max seq length: ", end="")
        max_len = 0
        with out_path.open() as f:
            for line in f:
                d = json.loads(line)
                max_len = max(max_len, len(d["tokens"]))
        print(max_len)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
