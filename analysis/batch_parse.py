#!/usr/bin/env python3
"""
Batch parser para 100 MPDs OMR.
Genera análisis estadístico cross-corpus:
- Distribución de piezas por set, año, theme.
- Top piezas globales.
- Top matrices globales.
- Patrones de chaining (deltas, bigramas).
- Y-layers cross-corpus.
- Cadencia de STEPs.
- BFC compliance.
- Custom parts inventory.
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict


T1_RE = re.compile(
    r'^1\s+(\S+)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\S+)$'
)


def parse_mpd_blocks(text):
    blocks = []
    current = None
    for line in text.split('\n'):
        m = re.match(r'^0 FILE\s+(.+?)\s*$', line)
        if m:
            if current is not None:
                blocks.append(current)
            current = {'file': m.group(1).strip(), 'lines': []}
            continue
        if re.match(r'^0 NOFILE\s*$', line):
            if current is not None:
                blocks.append(current)
                current = None
            continue
        if current is not None:
            current['lines'].append(line)
    if current is not None:
        blocks.append(current)
    return blocks


def parse_t1(line):
    m = T1_RE.match(line)
    if not m:
        return None
    g = m.groups()
    try:
        color = int(g[0])
    except ValueError:
        color = int(g[0], 16) if g[0].startswith(('0x', '0X')) else -1
    return {
        'color': color,
        'x': float(g[1]), 'y': float(g[2]), 'z': float(g[3]),
        'm': tuple(round(float(g[i]), 4) for i in range(4, 13)),
        'file': g[13],
    }


def analyze_one(mpd_path, meta):
    text = mpd_path.read_bytes().replace(b'\r\n', b'\n').decode('utf-8', errors='replace')
    blocks = parse_mpd_blocks(text)

    # meta['set_number'] may include qualifier like '1591-1'; strip it.
    full = str(meta['set_number'])
    if '-' in full:
        set_num = full.rsplit('-', 1)[0]
    else:
        set_num = full
    set_prefix = f"{set_num} - "
    s_prefix = f"s\\{set_num} - "
    hi_prefix = f"48\\{set_num} - "

    # sub-builds: FILE entries with .ldr extension
    main_ldr_blocks = [b for b in blocks
                       if b['file'].startswith(set_prefix) and b['file'].endswith('.ldr')]
    # Embedded custom parts
    embedded_dats = [b for b in blocks
                     if b['file'].startswith(set_prefix) and b['file'].endswith('.dat')]
    embedded_subs = [b for b in blocks if b['file'].startswith(s_prefix)]
    embedded_hires = [b for b in blocks if b['file'].startswith(hi_prefix)]

    # Aggregate all type-1 lines across sub-builds
    all_pieces = []
    sub_build_piece_counts = []
    for b in main_ldr_blocks:
        pieces = []
        for line in b['lines']:
            t1 = parse_t1(line)
            if t1:
                pieces.append(t1)
        all_pieces.extend(pieces)
        sub_build_piece_counts.append(len(pieces))

    # STEPs per sub-build
    step_counts = []
    for b in main_ldr_blocks:
        steps = sum(1 for l in b['lines'] if re.match(r'^0 STEP', l))
        step_counts.append(steps)

    # Master (first sub-build) steps
    master_steps = []
    if main_ldr_blocks:
        for line in main_ldr_blocks[0]['lines']:
            if re.match(r'^0 STEP', line):
                master_steps.append([])  # placeholder
            else:
                t1 = parse_t1(line)
                if t1 and master_steps:
                    master_steps[-1].append(t1)
                elif t1:
                    master_steps.append([t1])

    # Distributions
    files = Counter(p['file'] for p in all_pieces)
    colors = Counter(p['color'] for p in all_pieces)
    matrices = Counter(p['m'] for p in all_pieces)
    y_layers = Counter(round(p['y'], 1) for p in all_pieces)
    deltas = Counter()
    bigrams = Counter()
    for b in main_ldr_blocks:
        seq = []
        for line in b['lines']:
            t1 = parse_t1(line)
            if t1:
                seq.append(t1)
        for i in range(1, len(seq)):
            d = (round(seq[i]['x'] - seq[i-1]['x'], 1),
                 round(seq[i]['y'] - seq[i-1]['y'], 1),
                 round(seq[i]['z'] - seq[i-1]['z'], 1))
            deltas[d] += 1
        for i in range(1, len(seq)):
            bigrams[(seq[i-1]['file'], seq[i]['file'])] += 1

    # BFC compliance check
    has_bfc_certify = bool(re.search(r'^0 BFC CERTIFY', text, re.M))
    has_bfc_any = bool(re.search(r'^0 BFC\b', text, re.M))

    # Negative determinant count (reflections)
    neg_det = 0
    for p in all_pieces:
        a, b, c, d, e, f, g, h, i = p['m']
        det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
        if det < 0:
            neg_det += 1

    # bbox
    if all_pieces:
        xs = [p['x'] for p in all_pieces]
        ys = [p['y'] for p in all_pieces]
        zs = [p['z'] for p in all_pieces]
        bbox = [min(xs), min(ys), min(zs), max(xs), max(ys), max(zs)]
    else:
        bbox = None

    return {
        'meta': meta,
        'sub_build_count': len(main_ldr_blocks),
        'total_pieces': len(all_pieces),
        'sub_build_piece_counts': sub_build_piece_counts,
        'total_steps': sum(step_counts),
        'master_steps': len(master_steps),
        'master_steps_piece_counts': [len(s) for s in master_steps],
        'embedded_custom_parts': len(embedded_dats),
        'embedded_subparts': len(embedded_subs),
        'embedded_hires': len(embedded_hires),
        'unique_pieces': len(files),
        'unique_colors': len(colors),
        'unique_matrices': len(matrices),
        'top_30_pieces': files.most_common(30),
        'top_15_colors': colors.most_common(15),
        'top_15_y_layers': y_layers.most_common(15),
        'top_20_deltas': [
            {'dx': k[0], 'dy': k[1], 'dz': k[2], 'count': v}
            for k, v in deltas.most_common(20)
        ],
        'top_30_bigrams': [
            {'a': k[0], 'b': k[1], 'count': v}
            for k, v in bigrams.most_common(30)
        ],
        'has_bfc_certify': has_bfc_certify,
        'has_bfc_any': has_bfc_any,
        'neg_det_count': neg_det,
        'neg_det_ratio': (neg_det / len(all_pieces)) if all_pieces else 0,
        'bbox': bbox,
    }


def main():
    corpus_dir = Path('corpus/mpds')
    setlist = json.load(open('corpus/setlist_80s90s.json'))

    results = []
    for meta in setlist:
        # Filename in setlist.txt URLs uses set_number+qualifier pattern (e.g. 1591-1).
        # meta['set_number'] already contains '-qualifier' suffix in some entries.
        full = str(meta['set_number'])
        if '-' in full:
            num, q = full.rsplit('-', 1)
        else:
            num, q = full, meta.get('qualifier', '1')
        fname = f"{num}-{q}.mpd"
        path = corpus_dir / fname
        if not path.exists():
            print(f"WARN: missing {fname}", file=sys.stderr)
            continue
        try:
            r = analyze_one(path, meta)
            results.append(r)
            print(f"OK: {fname} ({r['total_pieces']} pieces, "
                  f"{r['sub_build_count']} sub-builds, "
                  f"theme={meta['theme']}, year={meta['year']})")
        except Exception as e:
            print(f"ERROR: {fname}: {e}", file=sys.stderr)

    # Aggregate cross-corpus stats
    agg = {
        'set_count': len(results),
        'total_pieces_all_sets': sum(r['total_pieces'] for r in results),
        'total_steps_all_sets': sum(r['total_steps'] for r in results),
        'total_sub_builds': sum(r['sub_build_count'] for r in results),
        'total_custom_parts': sum(r['embedded_custom_parts'] + r['embedded_subparts'] + r['embedded_hires'] for r in results),
        'pieces_per_set_stats': {
            'min': min(r['total_pieces'] for r in results),
            'max': max(r['total_pieces'] for r in results),
            'mean': sum(r['total_pieces'] for r in results) / len(results),
        },
        'global_top_50_pieces': Counter(),
        'global_top_20_colors': Counter(),
        'global_top_15_y_layers': Counter(),
        'global_top_30_deltas': Counter(),
        'global_top_50_bigrams': Counter(),
        'global_neg_det_count': 0,
        'global_total_pieces': 0,
        'bfc_certify_count': 0,
        'theme_breakdown': defaultdict(lambda: {'count': 0, 'pieces': 0, 'sets': []}),
        'decade_breakdown': {'80s': {'count': 0, 'pieces': 0}, '90s': {'count': 0, 'pieces': 0}},
    }

    for r in results:
        for p, c in r['top_30_pieces']:
            agg['global_top_50_pieces'][p] += c
        for c, n in r['top_15_colors']:
            agg['global_top_20_colors'][c] += n
        for y, n in r['top_15_y_layers']:
            agg['global_top_15_y_layers'][y] += n
        for d in r['top_20_deltas']:
            agg['global_top_30_deltas'][(d['dx'], d['dy'], d['dz'])] += d['count']
        for b in r['top_30_bigrams']:
            agg['global_top_50_bigrams'][(b['a'], b['b'])] += b['count']
        agg['global_neg_det_count'] += r['neg_det_count']
        agg['global_total_pieces'] += r['total_pieces']
        if r['has_bfc_certify']:
            agg['bfc_certify_count'] += 1
        theme = r['meta']['theme']
        agg['theme_breakdown'][theme]['count'] += 1
        agg['theme_breakdown'][theme]['pieces'] += r['total_pieces']
        agg['theme_breakdown'][theme]['sets'].append(r['meta']['set_number'])
        decade = '80s' if r['meta']['year'] < 1990 else '90s'
        agg['decade_breakdown'][decade]['count'] += 1
        agg['decade_breakdown'][decade]['pieces'] += r['total_pieces']

    agg['global_top_50_pieces'] = agg['global_top_50_pieces'].most_common(50)
    agg['global_top_20_colors'] = agg['global_top_20_colors'].most_common(20)
    agg['global_top_15_y_layers'] = agg['global_top_15_y_layers'].most_common(15)
    agg['global_top_30_deltas'] = [
        {'dx': k[0], 'dy': k[1], 'dz': k[2], 'count': v}
        for k, v in agg['global_top_30_deltas'].most_common(30)
    ]
    agg['global_top_50_bigrams'] = [
        {'a': k[0], 'b': k[1], 'count': v}
        for k, v in agg['global_top_50_bigrams'].most_common(50)
    ]
    agg['neg_det_ratio'] = (agg['global_neg_det_count'] / agg['global_total_pieces']) if agg['global_total_pieces'] else 0
    agg['theme_breakdown'] = dict(agg['theme_breakdown'])
    agg['decade_breakdown'] = dict(agg['decade_breakdown'])

    Path('analysis').mkdir(exist_ok=True)
    Path('analysis/cross_corpus_stats.json').write_text(json.dumps(agg, indent=2, ensure_ascii=False))
    Path('analysis/per_set_stats.json').write_text(json.dumps(results, indent=2, ensure_ascii=False))
    print('\n=== AGGREGATE ===')
    print(f"Sets analyzed: {agg['set_count']}")
    print(f"Total pieces: {agg['total_pieces_all_sets']}")
    print(f"Total sub-builds: {agg['total_sub_builds']}")
    print(f"Total custom parts: {agg['total_custom_parts']}")
    print(f"Mean pieces/set: {agg['pieces_per_set_stats']['mean']:.1f}")
    print(f"BFC CERTIFY ratio: {agg['bfc_certify_count']}/{agg['set_count']}")
    print(f"Neg-det (reflections) ratio: {agg['neg_det_ratio']*100:.3f}%")
    print(f"Top 10 pieces: {agg['global_top_50_pieces'][:10]}")
    print(f"Top 10 deltas: {agg['global_top_30_deltas'][:10]}")
    print(f"Top 10 bigrams: {agg['global_top_50_bigrams'][:10]}")


if __name__ == '__main__':
    main()
