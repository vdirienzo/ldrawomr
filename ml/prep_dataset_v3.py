"""
Town-focused dataset prep with theme conditioning.

Filters to Town-themed sets only (mid-range, 30-150 pieces) and emits
sequences with THEME_TOWN_* tokens at BOS for theme-conditioned generation.

Themes included:
- Town > Classic Town, Classic Town, Town (general)
- City > Police, Traffic, Construction, Fire, Airport, Farm, Harbor
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

TOWN_THEMES = {
    "Town > Classic Town", "Classic Town", "Town",
    "City > Police", "City > Traffic", "City > Construction",
    "City > Fire", "City > Airport", "City > Farm", "City > Harbor",
    "City",
}

THEME_KEYS = {
    "Town > Classic Town": "town_classic",
    "Classic Town": "town_classic",
    "Town": "town",
    "City > Police": "city_police",
    "City > Traffic": "city_traffic",
    "City > Construction": "city_construction",
    "City > Fire": "city_fire",
    "City > Airport": "city_airport",
    "City > Farm": "city_farm",
    "City > Harbor": "city_harbor",
    "City": "city",
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

THEME_TOKEN_NAMES = ["THEME_NONE"] + [f"THEME_{k.upper()}" for k in THEME_KEYS.values()]
VOCAB_BASE = 12
THEME_OFFSET = VOCAB_BASE
PIECE_OFFSET = THEME_OFFSET + len(THEME_TOKEN_NAMES)
VOCAB_SIZE = 2048


def build_vocab(per_set_path: Path, top_pieces: int = 512, top_colors: int = 64) -> dict:
    per_set = json.loads(per_set_path.read_text())
    base = Path("/home/user/Projects/ldraw")
    pieces, colors, matrices, xs, ys, zs = Counter(), Counter(), Counter(), Counter(), Counter(), Counter()

    # Filter to town sets only for vocabulary building too
    town_per_set = [r for r in per_set if r["meta"].get("theme", "") in TOWN_THEMES]
    n_scanned = 0
    for r in town_per_set:
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


def tokenize_mpd(mpd_path, vocab, theme_token):
    text = mpd_path.read_bytes().replace(b"\r\n", b"\n").decode("utf-8", errors="replace")
    piece_vocab = vocab["top_pieces"]
    color_vocab = vocab["top_colors"]
    x_buckets = vocab["x_buckets"]
    y_buckets = vocab["y_buckets"]
    z_buckets = vocab["z_buckets"]

    matrix_tuples = {tuple(m): vocab["matrix_offset"] + i for i, m in enumerate(vocab["matrices"])}

    def snap(val, buckets, base):
        if val in buckets:
            return base + buckets.index(val)
        if buckets:
            nearest = min(buckets, key=lambda b: abs(b - val))
            if abs(nearest - val) <= 12:
                return base + buckets.index(nearest)
        return None

    tokens = []
    if theme_token and theme_token in THEME_TOKEN_NAMES:
        tokens.append(THEME_OFFSET + THEME_TOKEN_NAMES.index(theme_token))
    else:
        tokens.append(THEME_OFFSET)  # THEME_NONE
    tokens.append(1)  # BOS

    for line in text.split("\n"):
        line = line.strip()
        if line.startswith("0 STEP") or line.startswith("0 !STEP"):
            tokens.append(3); continue
        if line.startswith("0 NOFILE"):
            tokens.append(4); continue
        if line.startswith("0 FILE"):
            tokens.append(5); continue
        m = T1_RE.match(line)
        if not m:
            continue
        g = m.groups()
        piece = g[13]
        tokens.append(vocab["piece_offset"] + piece_vocab.index(piece) if piece in piece_vocab else 6)
        try:
            color = int(g[0])
        except ValueError:
            color = -1
        tokens.append(vocab["color_offset"] + color_vocab.index(color) if color in color_vocab else 7)
        matrix = tuple(round(float(g[i]), 4) for i in range(4, 13))
        tokens.append(matrix_tuples.get(matrix, 8))
        x_tok = snap(round(float(g[1])), x_buckets, vocab["x_offset"])
        y_tok = snap(round(float(g[2])), y_buckets, vocab["y_offset"])
        z_tok = snap(round(float(g[3])), z_buckets, vocab["z_offset"])
        tokens.append(x_tok if x_tok is not None else 9)
        tokens.append(y_tok if y_tok is not None else 10)
        tokens.append(z_tok if z_tok is not None else 11)

    tokens.append(2)  # EOS
    return tokens


def main():
    base = Path("/home/user/Projects/ldraw")
    ml_dir = base / "ml"
    ml_dir.mkdir(exist_ok=True)

    print("Building town-only vocab v3...")
    vocab = build_vocab(base / "analysis" / "per_set_stats_1438.json")
    print(f"  pieces: {len(vocab['top_pieces'])}")
    print(f"  colors: {len(vocab['top_colors'])}")
    print(f"  theme tokens: {len(vocab['theme_token_names'])}")
    print(f"  total t1 scanned: {vocab['n_t1_scanned']}")
    (ml_dir / "vocab_v3.json").write_text(json.dumps(vocab, indent=2))

    print("\nTokenizing town-only mid-range sets...")
    per_set = json.loads((base / "analysis" / "per_set_stats_1438.json").read_text())
    town = [r for r in per_set if r["meta"].get("theme", "") in TOWN_THEMES and 30 <= r["total_pieces"] < 150]
    out_path = ml_dir / "dataset_v3.jsonl"
    n_seq = 0
    total_tokens = 0
    theme_distribution = Counter()
    with out_path.open("w") as fout:
        for r in town:
            cohort = r.get("cohort", "")
            num_full = r["meta"]["set_number"]
            mpd_dir = base / DIR_MAP.get(cohort, "")
            cands = list(mpd_dir.glob(f"{num_full}*.mpd"))
            if not cands:
                continue
            theme_full = r["meta"].get("theme", "")
            theme_short = THEME_KEYS.get(theme_full, "town")
            theme_token = f"THEME_{theme_short.upper()}"
            tokens = tokenize_mpd(cands[0], vocab, theme_token)
            if len(tokens) < 14:
                continue
            n_seq += 1
            total_tokens += len(tokens)
            theme_distribution[theme_token] += 1
            fout.write(json.dumps({"set": num_full, "theme": theme_token, "tokens": tokens}) + "\n")

    print(f"\nDataset v3 (town-only): {n_seq} sequences, {total_tokens:,} tokens")
    print(f"Mean: {total_tokens/n_seq:.0f} tokens/seq")
    print(f"\nTheme distribution:")
    for t, n in theme_distribution.most_common():
        print(f"  {n:3d}  {t}")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
