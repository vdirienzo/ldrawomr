#!/usr/bin/env python3
"""
Parser profundo: extrae secuencias step-by-step, transiciones de piezas,
distribución de offsets, matrices canónicas por tipo de pieza.
"""
import json
import re
from pathlib import Path
from collections import Counter, defaultdict


def normalize(text):
    return text.replace('\r\n', '\n')


def parse_mpd_blocks(text):
    """Returns list of {'file': name, 'lines': [...]}."""
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


T1_RE = re.compile(
    r'^1\s+(\S+)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+(\-?\d+(?:\.\d+)?)\s+'
    r'(\S+)$'
)


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
        'm': [float(g[i]) for i in range(4, 13)],
        'file': g[13],
    }


def matrix_str(m):
    return ' '.join(str(round(v, 4)) for v in m)


def analyze(mpd_path, set_num, label):
    txt = normalize(Path(mpd_path).read_bytes().decode('utf-8', errors='replace'))
    blocks = parse_mpd_blocks(txt)

    # Collect ALL type-1 lines from main .ldr files (skip embedded custom part .dat files)
    set_prefix = f"{set_num} - "
    s_prefix = f"s\\{set_num} - "
    hi_prefix = f"48\\{set_num} - "
    main_ldr_blocks = [b for b in blocks
                       if b['file'].startswith(set_prefix) and b['file'].endswith('.ldr')]
    # First main is the master scene; rest are sub-builds (still count their pieces).
    # We want a unified view of how pieces are placed across all sub-builds.
    all_pieces = []
    for b in main_ldr_blocks:
        for line in b['lines']:
            t1 = parse_t1(line)
            if t1:
                t1['source'] = b['file'][len(set_prefix):]
                all_pieces.append(t1)

    # Step sequence in master only
    master_pieces = []
    steps = []  # list of (step_index, [pieces])
    current_step_pieces = []
    if main_ldr_blocks:
        for line in main_ldr_blocks[0]['lines']:
            if re.match(r'^0 STEP', line):
                steps.append(current_step_pieces)
                current_step_pieces = []
                continue
            t1 = parse_t1(line)
            if t1:
                master_pieces.append(t1)
                current_step_pieces.append(t1)
        steps.append(current_step_pieces)

    # For bigrams/trigrams, we need to flatten across ALL sub-builds
    # since 10218 has a master scene with 0 pieces (just refs).
    # We concatenate each sub-build's piece list, resetting between blocks.
    all_sequences = []
    for b in main_ldr_blocks:
        seq = []
        for line in b['lines']:
            t1 = parse_t1(line)
            if t1:
                seq.append(t1)
        if seq:
            all_sequences.append(seq)

    # Bigrams across all sequences
    bigrams = Counter()
    trigrams = Counter()
    for seq in all_sequences:
        for i in range(len(seq) - 1):
            b = (seq[i]['file'], seq[i+1]['file'])
            bigrams[b] += 1
        for i in range(len(seq) - 2):
            t = (seq[i]['file'], seq[i+1]['file'], seq[i+2]['file'])
            trigrams[t] += 1

    # Y-layer distribution (all_pieces)
    y_layers = Counter()
    for p in all_pieces:
        y_layers[round(p['y'], 1)] += 1

    # Position offsets between consecutive pieces (per sequence, then aggregate)
    position_deltas = Counter()
    for seq in all_sequences:
        for i in range(len(seq) - 1):
            dx = round(seq[i+1]['x'] - seq[i]['x'], 2)
            dy = round(seq[i+1]['y'] - seq[i]['y'], 2)
            dz = round(seq[i+1]['z'] - seq[i]['z'], 2)
            position_deltas[(dx, dy, dz)] += 1

    # Matrices by piece type (top pieces only)
    matrices_by_piece = defaultdict(Counter)
    for p in all_pieces:
        matrices_by_piece[p['file']][matrix_str(p['m'])] += 1
    top_pieces_matrix = {}
    for piece, mc in matrices_by_piece.items():
        if sum(mc.values()) >= 3:  # only pieces used 3+ times
            top_pieces_matrix[piece] = mc.most_common(5)

    # Files referenced
    file_counter = Counter(p['file'] for p in all_pieces)
    color_counter = Counter(p['color'] for p in all_pieces)

    # Unique custom parts embedded
    embedded_dats = sorted({b['file'][len(set_prefix):] for b in blocks
                            if b['file'].startswith(set_prefix) and b['file'].endswith('.dat')})
    embedded_subs = sorted({b['file'][len(s_prefix):] for b in blocks
                            if b['file'].startswith(s_prefix)})
    embedded_hires = sorted({b['file'][len(hi_prefix):] for b in blocks
                             if b['file'].startswith(hi_prefix)})

    # Same-piece deltas across all sequences
    same_piece_patterns = defaultdict(list)
    for seq in all_sequences:
        for i in range(len(seq) - 1):
            if seq[i]['file'] == seq[i+1]['file']:
                d = (round(seq[i+1]['x'] - seq[i]['x'], 1),
                     round(seq[i+1]['y'] - seq[i]['y'], 1),
                     round(seq[i+1]['z'] - seq[i]['z'], 1))
                same_piece_patterns[seq[i]['file']].append(d)
    same_piece_deltas = {}
    for piece, deltas in same_piece_patterns.items():
        if len(deltas) >= 2:
            c = Counter(deltas)
            same_piece_deltas[piece] = c.most_common(3)

    return {
        'set': label,
        'set_number': set_num,
        'mpd': mpd_path,
        'total_pieces_in_subbuilds': len(all_pieces),
        'master_piece_count': len(master_pieces),
        'sub_model_count': len(main_ldr_blocks),
        'sub_model_count_with_pieces': len(all_sequences),
        'step_count': len(steps),
        'pieces_per_step_stats': {
            'mean': (sum(len(s) for s in steps) / max(1, len(steps))),
            'min': min((len(s) for s in steps), default=0),
            'max': max((len(s) for s in steps), default=0),
            'median': sorted(len(s) for s in steps)[len(steps)//2] if steps else 0,
        },
        'steps_size_distribution': dict(Counter(len(s) for s in steps)),
        'top_30_pieces': file_counter.most_common(30),
        'top_10_colors': color_counter.most_common(10),
        'unique_pieces': len(file_counter),
        'unique_colors': len(color_counter),
        'top_20_y_layers': y_layers.most_common(20),
        'top_20_position_deltas': [
            {'dx': k[0], 'dy': k[1], 'dz': k[2], 'count': v}
            for k, v in position_deltas.most_common(20)
        ],
        'top_20_bigrams': [
            {'from': k[0], 'to': k[1], 'count': v}
            for k, v in bigrams.most_common(20)
        ],
        'top_15_trigrams': [
            {'a': k[0], 'b': k[1], 'c': k[2], 'count': v}
            for k, v in trigrams.most_common(15)
        ],
        'top_pieces_matrices': top_pieces_matrix,
        'same_piece_deltas': same_piece_deltas,
        'embedded_custom_parts_count': len(embedded_dats),
        'embedded_custom_subparts_count': len(embedded_subs),
        'embedded_hires_count': len(embedded_hires),
        'embedded_custom_parts_sample': embedded_dats[:10],
        'embedded_custom_subparts_sample': embedded_subs[:10],
        'embedded_hires_sample': embedded_hires[:10],
    }


if __name__ == '__main__':
    out = {
        '10252_VW_Beetle': analyze('corpus/10252-1.mpd', '10252', '10252 Volkswagen Beetle'),
        '10218_PetShop':   analyze('corpus/10218-1.mpd', '10218', '10218 Pet Shop'),
    }
    Path('analysis').mkdir(exist_ok=True)
    Path('analysis/deep_stats.json').write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print('OK')
    print('Master pieces:', out['10252_VW_Beetle']['master_piece_count'], '/',
          out['10218_PetShop']['master_piece_count'])
    print('Top pieces 10252:', out['10252_VW_Beetle']['top_30_pieces'][:10])
    print('Top pieces 10218:', out['10218_PetShop']['top_30_pieces'][:10])
