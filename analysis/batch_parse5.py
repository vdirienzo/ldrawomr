#!/usr/bin/env python3
"""
Parser unificado cross-corpus 4.0: 1438 sets OMR (8 cohorts) + 378 sets seymouria.pl.
Total: 1816 sets across 9 cohorts.

New cohort (Plan E):
- seymouria: 378 sets from seymouria.pl that are NOT in the OMR corpus.
  Source: https://www.seymouria.pl/Download/official-lego-sets-ldr.php
  URL pattern: https://www.seymouria.pl/Download/OfficialLegoSets_LDR/<file>

Genera cross_corpus4_stats.json + per_set_stats_<N>.json.
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


def analyze_one(mpd_path, meta, cohort):
    text = mpd_path.read_bytes().replace(b'\r\n', b'\n').decode('utf-8', errors='replace')
    blocks = parse_mpd_blocks(text)

    full = str(meta['set_number'])
    if '-' in full:
        set_num, q = full.rsplit('-', 1)
    else:
        set_num, q = full, meta.get('qualifier', '1')
    set_prefix = f"{set_num} - "
    s_prefix = f"s\\{set_num} - "
    hi_prefix = f"48\\{set_num} - "

    main_ldr_blocks = [b for b in blocks
                       if b['file'].startswith(set_prefix) and b['file'].endswith('.ldr')]
    embedded_dats = [b for b in blocks
                     if b['file'].startswith(set_prefix) and b['file'].endswith('.dat')]
    embedded_subs = [b for b in blocks if b['file'].startswith(s_prefix)]
    embedded_hires = [b for b in blocks if b['file'].startswith(hi_prefix)]

    all_pieces = []
    sub_build_piece_counts = []
    step_counts = []
    for b in main_ldr_blocks:
        pieces = []
        for line in b['lines']:
            t1 = parse_t1(line)
            if t1:
                pieces.append(t1)
        all_pieces.extend(pieces)
        sub_build_piece_counts.append(len(pieces))
        steps = sum(1 for l in b['lines'] if re.match(r'^0 STEP', l))
        step_counts.append(steps)

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

    has_bfc_certify = bool(re.search(r'^0 BFC CERTIFY', text, re.M))
    has_bfc_any = bool(re.search(r'^0 BFC\b', text, re.M))

    neg_det = 0
    for p in all_pieces:
        a, b, c, d, e, f, g, h, i = p['m']
        det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
        if det < 0:
            neg_det += 1

    if all_pieces:
        xs = [p['x'] for p in all_pieces]
        ys = [p['y'] for p in all_pieces]
        zs = [p['z'] for p in all_pieces]
        bbox = [min(xs), min(ys), min(zs), max(xs), max(ys), max(zs)]
    else:
        bbox = None

    return {
        'meta': meta,
        'cohort': cohort,
        'sub_build_count': len(main_ldr_blocks),
        'total_pieces': len(all_pieces),
        'sub_build_piece_counts': sub_build_piece_counts,
        'total_steps': sum(step_counts),
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


def aggregate(results, cohort_label):
    agg = {
        'cohort': cohort_label,
        'set_count': len(results),
        'total_pieces': sum(r['total_pieces'] for r in results),
        'total_sub_builds': sum(r['sub_build_count'] for r in results),
        'total_custom_parts': sum(
            r['embedded_custom_parts'] + r['embedded_subparts'] + r['embedded_hires']
            for r in results
        ),
        'pieces_per_set_stats': {
            'min': min(r['total_pieces'] for r in results) if results else 0,
            'max': max(r['total_pieces'] for r in results) if results else 0,
            'mean': sum(r['total_pieces'] for r in results) / len(results) if results else 0,
        },
        'steps_per_set_stats': {
            'mean': sum(r['total_steps'] for r in results) / len(results) if results else 0,
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
        'decade_breakdown': defaultdict(lambda: {'count': 0, 'pieces': 0}),
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
        theme = r['meta'].get('theme', 'Unknown')
        agg['theme_breakdown'][theme]['count'] += 1
        agg['theme_breakdown'][theme]['pieces'] += r['total_pieces']
        agg['theme_breakdown'][theme]['sets'].append(r['meta']['set_number'])
        year = r['meta'].get('year', 0)
        decade = f"{(year // 10) * 10}s"
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
    return agg


def main():
    Path('analysis').mkdir(exist_ok=True)

    # Cohort 1: 80s/90s
    setlist_old = json.load(open('corpus/setlist_80s90s.json'))
    results_old = []
    for meta in setlist_old:
        full = str(meta['set_number'])
        if '-' in full:
            num, q = full.rsplit('-', 1)
        else:
            num, q = full, meta.get('qualifier', '1')
        path = Path('corpus/mpds') / f"{num}-{q}.mpd"
        if not path.exists():
            continue
        try:
            r = analyze_one(path, meta, cohort='80s90s')
            results_old.append(r)
        except Exception as e:
            print(f"ERROR old: {num}: {e}", file=sys.stderr)

    # Cohort 2: kids
    setlist_kids = json.load(open('corpus/setlist_kids.json'))
    # Cohort 3: classic (Plan C, pre-2000 themes uniform)
    try:
        setlist_classic = json.load(open('corpus/setlist_classic.json'))
    except FileNotFoundError:
        setlist_classic = []
    results_kids = []
    for meta in setlist_kids:
        full = str(meta['set_number'])
        if '-' in full:
            num, q = full.rsplit('-', 1)
        else:
            num, q = full, meta.get('qualifier', '1')
        # handle sub_model field
        if meta.get('sub_model'):
            fname = f"{num}-{q}_{meta['sub_model']}.mpd"
        else:
            fname = f"{num}-{q}.mpd"
        path = Path('corpus/mpds_kids') / fname
        if not path.exists():
            # try the base name
            path = Path('corpus/mpds_kids') / f"{num}-{q}.mpd"
        if not path.exists():
            print(f"WARN missing: {fname}", file=sys.stderr)
            continue
        try:
            r = analyze_one(path, meta, cohort='kids')
            results_kids.append(r)
        except Exception as e:
            print(f"ERROR kids: {num}: {e}", file=sys.stderr)

    results_classic = []
    for meta in setlist_classic:
        full = str(meta['set_number'])
        if '-' in full:
            num, q = full.rsplit('-', 1)
        else:
            num, q = full, meta.get('qualifier', '1')
        # Handle multi-model URLs like "722-1_Helicopter.mpd"
        base = f"{num}-{q}"
        candidates = list(Path('corpus/mpds_classic').glob(f"{base}*.mpd"))
        if not candidates:
            print(f"WARN missing classic: {base}", file=sys.stderr)
            continue
        path = candidates[0]
        try:
            r = analyze_one(path, meta, cohort='classic')
            results_classic.append(r)
        except Exception as e:
            print(f"ERROR classic: {num}: {e}", file=sys.stderr)

    # New cohorts (Plan D): modern, technic, specialty, licensed, classic_gaps
    new_cohorts = ['modern', 'technic', 'specialty', 'licensed', 'classic_gaps', 'seymouria']
    new_results = {}
    for cohort in new_cohorts:
        setlist_path = f'corpus/setlist_{cohort}.json'
        dir_path = f'corpus/mpds_{cohort}'
        try:
            setlist = json.load(open(setlist_path))
        except FileNotFoundError:
            print(f"WARN no setlist for {cohort}", file=sys.stderr)
            new_results[cohort] = []
            continue
        results = []
        for meta in setlist:
            # Normalize meta to have set_number (legacy) or derive from full/number
            if 'set_number' not in meta:
                if 'full' in meta:
                    meta['set_number'] = meta['full']
                elif 'number' in meta and 'qualifier' in meta:
                    meta['set_number'] = f"{meta['number']}-{meta['qualifier']}"
                else:
                    print(f"WARN {cohort}: meta missing set_number: {meta}", file=sys.stderr)
                    continue
            url = meta.get('url', '')
            fname = meta.get('filename') or (url.rsplit('/', 1)[1] if url else '')
            # URL-decode the fname if it was URL-encoded
            import urllib.parse as _up
            fname_decoded = _up.unquote(fname)
            path = Path(dir_path) / fname_decoded
            if not path.exists():
                # try base name without suffix
                full = str(meta['set_number'])
                if '-' in full:
                    num, q = full.rsplit('-', 1)
                else:
                    num, q = full, meta.get('qualifier', '1')
                base = f"{num}-{q}"
                # Search both .mpd and .ldr variants (seymouria mixes extensions)
                candidates = list(Path(dir_path).glob(f"{num} - *{base[-1]}*.mpd")) + \
                             list(Path(dir_path).glob(f"{base}*.mpd")) + \
                             list(Path(dir_path).glob(f"{base}*.ldr"))
                if candidates:
                    path = candidates[0]
                else:
                    print(f"WARN missing {cohort}: {fname_decoded}", file=sys.stderr)
                    continue
            try:
                r = analyze_one(path, meta, cohort=cohort)
                results.append(r)
            except Exception as e:
                print(f"ERROR {cohort}: {meta.get('set_number', '?')}: {e}", file=sys.stderr)
        new_results[cohort] = results
        print(f'{cohort} parsed: {len(results)} sets')

    print(f'\n80s/90s parsed: {len(results_old)} sets')
    print(f'Kids parsed: {len(results_kids)} sets')
    print(f'Classic parsed: {len(results_classic)} sets')

    # Aggregate per cohort
    agg_old = aggregate(results_old, '80s90s')
    agg_kids = aggregate(results_kids, 'kids')
    agg_classic = aggregate(results_classic, 'classic')
    agg_modern = aggregate(new_results['modern'], 'modern')
    agg_technic = aggregate(new_results['technic'], 'technic')
    agg_specialty = aggregate(new_results['specialty'], 'specialty')
    agg_licensed = aggregate(new_results['licensed'], 'licensed')
    agg_classic_gaps = aggregate(new_results['classic_gaps'], 'classic_gaps')
    agg_seymouria = aggregate(new_results['seymouria'], 'seymouria')

    # Global (1438 OMR + 378 seymouria = 1816 sets if all downloaded)
    all_results_full = (results_old + results_kids + results_classic +
                        new_results['modern'] + new_results['technic'] +
                        new_results['specialty'] + new_results['licensed'] +
                        new_results['classic_gaps'] +
                        new_results['seymouria'])
    agg_all = aggregate(all_results_full, f'all_{len(all_results_full)}')

    out = {
        'cohort_80s90s': agg_old,
        'cohort_kids': agg_kids,
        'cohort_classic': agg_classic,
        'cohort_modern': agg_modern,
        'cohort_technic': agg_technic,
        'cohort_specialty': agg_specialty,
        'cohort_licensed': agg_licensed,
        'cohort_classic_gaps': agg_classic_gaps,
        'cohort_seymouria': agg_seymouria,
        f'cohort_all_{len(all_results_full)}': agg_all,
    }

    Path('analysis/cross_corpus4_stats.json').write_text(json.dumps(out, indent=2, ensure_ascii=False))
    Path(f'analysis/per_set_stats_{len(all_results_full)}.json').write_text(json.dumps(all_results_full, indent=2, ensure_ascii=False))

    # Print summary for each cohort
    for name, agg in [('80s/90s', agg_old), ('Kids', agg_kids), ('Classic', agg_classic),
                      ('Modern', agg_modern), ('Technic', agg_technic),
                      ('Specialty', agg_specialty), ('Licensed', agg_licensed),
                      ('Classic_gaps', agg_classic_gaps),
                      ('Seymouria', agg_seymouria)]:
        print(f"\n=== COHORT {name} ===")
        print(f"  sets={agg['set_count']}, pieces={agg['total_pieces']}")
        print(f"  custom={agg['total_custom_parts']}, BFC CERTIFY={agg['bfc_certify_count']}/{agg['set_count']}")
        print(f"  neg_det_ratio={agg['neg_det_ratio']*100:.3f}%")
        print(f"  top pieces: {agg['global_top_50_pieces'][:5]}")
        print(f"  top deltas: {agg['global_top_30_deltas'][:5]}")

    print(f"\n=== ALL {len(all_results_full)} ===")
    print(f"  sets={agg_all['set_count']}, pieces={agg_all['total_pieces']}")
    print(f"  custom={agg_all['total_custom_parts']}, BFC CERTIFY={agg_all['bfc_certify_count']}/{agg_all['set_count']}")
    print(f"  neg_det_ratio={agg_all['neg_det_ratio']*100:.3f}%")
    print(f"  top pieces: {agg_all['global_top_50_pieces'][:10]}")
    print(f"  top deltas: {agg_all['global_top_30_deltas'][:5]}")


if __name__ == '__main__':
    main()
