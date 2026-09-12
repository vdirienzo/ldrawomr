"""
Dataset preparation v2: theme conditioning + sliding window.

Improvements over v1 (prep_dataset.py):
- Theme tokens prepended at BOS, enabling theme-conditioned generation.
- Sliding-window chunking: each long sequence produces multiple training samples.
- Larger vocabulary: top 512 pieces, top 64 colors.
- Same coordinate quantization but with theme awareness.

Output: ml/dataset_v2.jsonl (one chunk per line) + ml/vocab_v2.json.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

NUM = r"(\-?\d+(?:\.\d+)?)"
T1_RE = re.compile(
    r"^1\s+(\S+)\s+"
    + NUM + r"\s+" + NUM + r"\s+" + NUM + r"\s+"
    + (NUM + r"\s+") * 8 + NUM + r"\s+(.+)$"
)

# Canonical themes with enough samples for conditioning (>=10 mid-range sets).
# Mapped to simple short keys for token names.
THEME_KEYS = {
    "Town > Classic Town": "town_classic",
    "Classic Town": "town_classic",
    "Town": "town",
    "City > Police": "city_police",
    "City > Traffic": "city_traffic",
    "City > Construction": "city_construction",
    "Racers": "racers",
    "Brickheadz": "brickheadz",
    "Star Wars": "star_wars",
    "Creator > Creator 3-in-1": "creator_3in1",
    "Creator > Designer Sets": "creator_designer",
    "Creator > Creator Expert": "creator_expert",
    "Friends": "friends",
    "Fabuland": "fabuland",
    "Technic": "technic",
    "Technic > Expert Builder": "technic_expert",
    "Western": "western",
    "Space > Classic Space": "space_classic",
    "Space": "space",
    "Train > 9V": "train_9v",
    "Train": "train",
    "Boat": "boat",
    "Castle": "castle",
    "Pirates > Pirates I": "pirates",
    "City > Fire": "city_fire",
    "City > Airport": "city_airport",
    "City > Farm": "city_farm",
    "City > Harbor": "city_harbor",
    "Architecture": "architecture",
    "LEGO Ideas and CUUSOO": "ideas",
    "Architecture > Skylines": "architecture_skyline",
    "Modular Buildings": "modular",
    "Icons": "icons",
    "Mixels": "mixels",
}

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

BFC_TOP_MATRICES = [
    [1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, -1, 0, 0],
    [0, 0, -1, 0, 1, 0, 1, 0, 0],
    [-1, 0, 0, 0, 1, 0, 0, 0, -1],
    [1, 0, 0, 0, 0, -1, 0, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, -1, 0],
    [0, -1, 0, 1, 0, 0, 0, 0, 1],
    [-1, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, -1, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, -1, -1, 0, 0],
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
    [1, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, -1, 0, 0],
]

# Special tokens (12 base + 64 theme tokens)
SPECIAL_TOKENS = [
    "PAD", "BOS", "EOS", "STEP", "NOFILE", "FILE",
    "PIECE_UNK", "COLOR_UNK", "MATRIX_UNK", "X_UNK", "Y_UNK", "Z_UNK",
]
THEME_TOKEN_NAMES = ["THEME_NONE"] + [f"THEME_{key.upper()}" for key in THEME_KEYS.keys()]

VOCAB_BASE = 12  # 0..11
THEME_OFFSET = VOCAB_BASE  # 12..12+len(THEME_TOKEN_NAMES)
PIECE_OFFSET = THEME_OFFSET + len(THEME_TOKEN_NAMES)
VOCAB_SIZE = 2048  # padded for headroom


def build_vocab(per_set_path: Path, top_pieces: int = 512, top_colors: int = 64) -> dict:
    per_set = json.loads(per_set_path.read_text())
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

    return {
        "vocab_size": VOCAB_SIZE,
        "n_t1_scanned": n_scanned,
        "special_tokens": SPECIAL_TOKENS,
        "theme_token_names": THEME_TOKEN_NAMES,
        "theme_offset": THEME_OFFSET,
        "piece_offset": PIECE_OFFSET,
        "top_pieces": [p for p, _ in pieces.most_common(top_pieces)],
        "color_offset": PIECE_OFFSET + top_pieces,
        "top_colors": [c for c, _ in colors.most_common(top_colors)],
        "matrix_offset": PIECE_OFFSET + top_pieces + top_colors,
        "matrices": BFC_TOP_MATRICES,
        "x_offset": PIECE_OFFSET + top_pieces + top_colors + len(BFC_TOP_MATRICES),
        "x_buckets": [v for v, _ in xs.most_common(96)],
        "y_offset": PIECE_OFFSET + top_pieces + top_colors + len(BFC_TOP_MATRICES) + 96,
        "y_buckets": [v for v, _ in ys.most_common(48)],
        "z_offset": PIECE_OFFSET + top_pieces + top_colors + len(BFC_TOP_MATRICES) + 96 + 48,
        "z_buckets": [v for v, _ in zs.most_common(96)],
    }


def tokenize_mpd(mpd_path: Path, vocab: dict, theme: str | None) -> list:
    text = mpd_path.read_bytes().replace(b"\r\n", b"\n").decode("utf-8", errors="replace")
    piece_vocab = vocab["top_pieces"]
    color_vocab = vocab["top_colors"]
    x_buckets = vocab["x_buckets"]
    y_buckets = vocab["y_buckets"]
    z_buckets = vocab["z_buckets"]
    chunk_size = 768
    stride = 384  # 50% overlap

    def snap(val, buckets, base):
        if val in buckets:
            return base + buckets.index(val)
        if buckets:
            nearest = min(buckets, key=lambda b: abs(b - val))
            if abs(nearest - val) <= 12:
                return base + buckets.index(nearest)
        return None

    full_tokens = []
    # Theme token at start
    if theme and theme in THEME_TOKEN_NAMES:
        full_tokens.append(THEME_OFFSET + THEME_TOKEN_NAMES.index(theme))
    else:
        full_tokens.append(THEME_OFFSET + THEME_TOKEN_NAMES.index("THEME_NONE"))  # placeholder
    full_tokens.append(1)  # BOS

    matrix_tuples = {tuple(m): vocab["matrix_offset"] + i for i, m in enumerate(vocab["matrices"])}

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("0 STEP") or line.startswith("0 !STEP"):
            full_tokens.append(3)
            continue
        if line.startswith("0 NOFILE"):
            full_tokens.append(4)
            continue
        if line.startswith("0 FILE"):
            full_tokens.append(5)
            continue
        m = T1_RE.match(line)
        if not m:
            continue
        g = m.groups()
        piece = g[13]
        full_tokens.append(vocab["piece_offset"] + piece_vocab.index(piece) if piece in piece_vocab else 6)
        try:
            color = int(g[0])
        except ValueError:
            color = -1
        full_tokens.append(vocab["color_offset"] + color_vocab.index(color) if color in color_vocab else 7)
        matrix = tuple(round(float(g[i]), 4) for i in range(4, 13))
        full_tokens.append(matrix_tuples.get(matrix, 8))
        x_tok = snap(round(float(g[1])), x_buckets, vocab["x_offset"])
        y_tok = snap(round(float(g[2])), y_buckets, vocab["y_offset"])
        z_tok = snap(round(float(g[3])), z_buckets, vocab["z_offset"])
        full_tokens.append(x_tok if x_tok is not None else 9)
        full_tokens.append(y_tok if y_tok is not None else 10)
        full_tokens.append(z_tok if z_tok is not None else 11)

    full_tokens.append(2)  # EOS
    if len(full_tokens) < chunk_size + 2:
        yield full_tokens
        return
    # Sliding window chunks
    n = 0
    for start in range(1, len(full_tokens) - chunk_size, stride):
        chunk = [full_tokens[0], full_tokens[1]] + full_tokens[start:start + chunk_size]
        chunk[-1] = 2  # force EOS at end
        yield chunk
        n += 1
        if n > 4:  # cap chunks per set to avoid one big set dominating
            break


def main():
    base = Path("/home/user/Projects/ldraw")
    ml_dir = base / "ml"
    ml_dir.mkdir(exist_ok=True)

    print("Building vocab v2...")
    vocab = build_vocab(base / "analysis" / "per_set_stats_1438.json")
    print(f"  pieces: {len(vocab['top_pieces'])}")
    print(f"  colors: {len(vocab['top_colors'])}")
    print(f"  matrices: {len(vocab['matrices'])}")
    print(f"  x_buckets: {len(vocab['x_buckets'])}, y: {len(vocab['y_buckets'])}, z: {len(vocab['z_buckets'])}")
    print(f"  theme tokens: {len(vocab['theme_token_names'])}")
    print(f"  total vocab size (padded): {vocab['vocab_size']}")

    (ml_dir / "vocab_v2.json").write_text(json.dumps(vocab, indent=2))

    print("\nTokenizing + sliding-window chunking...")
    per_set = json.loads((base / "analysis" / "per_set_stats_1438.json").read_text())
    raw_count = 0
    chunk_count = 0
    total_tokens = 0
    theme_distribution = Counter()
    out_path = ml_dir / "dataset_v2.jsonl"
    with out_path.open("w") as fout:
        for r in per_set:
            cohort = r.get("cohort", "")
            num_full = r["meta"]["set_number"]
            mpd_dir = base / DIR_MAP.get(cohort, "")
            cands = list(mpd_dir.glob(f"{num_full}*.mpd"))
            if not cands:
                continue
            raw_count += 1
            theme_full = r["meta"].get("theme", "")
            theme_short = THEME_KEYS.get(theme_full)
            theme_token = f"THEME_{theme_short.upper()}" if theme_short else None
            for tokens in tokenize_mpd(cands[0], vocab, theme_token):
                chunk_count += 1
                total_tokens += len(tokens)
                if theme_token:
                    theme_distribution[theme_token] += 1
                fout.write(json.dumps({"set": num_full, "theme": theme_token, "tokens": tokens}) + "\n")

    print(f"\nDataset v2: {chunk_count} chunks from {raw_count} sets, {total_tokens:,} tokens")
    print(f"Mean chunk length: {total_tokens / max(chunk_count, 1):.0f}")
    print(f"\nTheme distribution (top 15):")
    for t, n in theme_distribution.most_common(15):
        print(f"  {n:5d}  {t}")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
