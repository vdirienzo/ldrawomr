#!/usr/bin/env python3
"""
Parser LDraw OMR MPD -> JSON estructurado.
Extrae:
- Lista de sub-modelos (0 FILE ...).
- Piezas (line type 1) por sub-modelo: color, x,y,z, matriz 3x3, archivo.
- STEPs (líneas 0 STEP).
- Custom parts (archivos cuyo nombre empieza con el set-number).
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter, defaultdict


def parse_mpd(path):
    raw = Path(path).read_bytes()
    # Normalize CRLF → LF for parsing
    txt = raw.replace(b'\r\n', b'\n').decode('utf-8', errors='replace')
    # split into blocks by FILE/NOFILE
    blocks = []
    current = None
    for line in txt.splitlines():
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


def parse_blocks(blocks, set_number):
    """Split blocks into main sub-models (build steps) and custom parts."""
    set_prefix = f"{set_number} - "
    s_prefix = f"s\\{set_number} - "
    hi_prefix = f"48\\{set_number} - "
    main_blocks = []
    custom_parts = []
    for b in blocks:
        fname = b['file']
        if fname.startswith(set_prefix):
            bare = fname[len(set_prefix):]
            if bare.endswith('.ldr'):
                main_blocks.append({'name': bare[:-4], **b, 'kind': 'submodel'})
            elif bare.endswith('.dat'):
                custom_parts.append({'name': bare, **b, 'kind': 'custom_part'})
        elif fname.startswith(s_prefix):
            bare = fname[len(s_prefix):]
            custom_parts.append({'name': f"s/{bare}", **b, 'kind': 'custom_subpart'})
        elif fname.startswith(hi_prefix):
            bare = fname[len(hi_prefix):]
            custom_parts.append({'name': f"48/{bare}", **b, 'kind': 'custom_hires'})
    return main_blocks, custom_parts


def parse_type1(line):
    """Parse a type-1 line (sub-file reference)."""
    m = re.match(
        r'^1\s+(\S+)\s+'           # color (or 0x2RRGGBB)
        r'(-?\d+(?:\.\d+)?)\s+'    # x
        r'(-?\d+(?:\.\d+)?)\s+'    # y
        r'(-?\d+(?:\.\d+)?)\s+'    # z
        r'(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+'  # a b c
        r'(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+'  # d e f
        r'(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+(-?\d+(?:\.\d+)?)\s+'  # g h i
        r'(\S+)$',                  # filename
        line
    )
    if not m:
        return None
    parts = m.groups()
    return {
        'color_raw': parts[0],
        'color': int(parts[0]) if parts[0].startswith(('0x', '0X')) is False and not parts[0].startswith('0x') else int(parts[0], 16),
        'x': float(parts[1]),
        'y': float(parts[2]),
        'z': float(parts[3]),
        'a': float(parts[4]), 'b': float(parts[5]), 'c': float(parts[6]),
        'd': float(parts[7]), 'e': float(parts[8]), 'f': float(parts[9]),
        'g': float(parts[10]), 'h': float(parts[11]), 'i': float(parts[12]),
        'file': parts[13],
    }


def matrix_canonical(m):
    """Canonicalize a rotation matrix: tuple of 9 ints/floats, sign-respecting."""
    # Represent as 9-tuple of the integer matrix elements when possible.
    cells = [m[k] for k in 'abcdefghi']
    return tuple(round(v, 4) for v in cells)


def matrix_det(m):
    return (m['a']*(m['e']*m['i'] - m['f']*m['h'])
          - m['b']*(m['d']*m['i'] - m['f']*m['g'])
          + m['c']*(m['d']*m['h'] - m['e']*m['g']))


def analyze_set(mpd_path, set_number, set_label):
    blocks = parse_mpd(mpd_path)
    main_blocks, custom_parts = parse_blocks(blocks, set_number)
    # The first main block is the master scene; the rest are referenced sub-builds.
    # Collect all type-1 lines from main blocks (step-by-step build).
    all_instances = []
    steps_in_master = []
    pieces_per_step = []
    current_step = {'step': 0, 'pieces': []}
    master_block = main_blocks[0] if main_blocks else None
    master_pieces = []
    if master_block:
        for line in master_block['lines']:
            if re.match(r'^0 STEP', line):
                steps_in_master.append(len(pieces_per_step))
                pieces_per_step = []
                continue
            t1 = parse_type1(line)
            if t1:
                # Exclude embedded custom parts (those would be inlined sub-builds too)
                all_instances.append(t1)
                master_pieces.append(t1)
                current_step['pieces'].append(t1)
                pieces_per_step.append(t1)
        if pieces_per_step:
            steps_in_master.append(len(pieces_per_step))

    # Distributions
    file_counter = Counter(p['file'] for p in master_pieces)
    color_counter = Counter(p['color'] for p in master_pieces)
    matrix_counter = Counter(matrix_canonical(p) for p in master_pieces)
    y_values = Counter(round(p['y'], 1) for p in master_pieces)

    # Bounding box
    if master_pieces:
        xs = [p['x'] for p in master_pieces]
        ys = [p['y'] for p in master_pieces]
        zs = [p['z'] for p in master_pieces]
        bbox = {'x': (min(xs), max(xs)), 'y': (min(ys), max(ys)), 'z': (min(zs), max(zs))}
    else:
        bbox = None

    # Step statistics
    step_lens = [len(b['lines']) for b in main_blocks[1:]]  # sub-builds
    sub_build_pieces = []
    for b in main_blocks[1:]:
        for line in b['lines']:
            t1 = parse_type1(line)
            if t1:
                sub_build_pieces.append(t1)

    # Custom parts content: try to extract primitives used
    custom_part_summary = []
    for cp in custom_parts:
        primitives = []
        for line in cp['lines']:
            t1 = parse_type1(line)
            if t1 and not t1['file'].endswith('.ldr'):
                primitives.append(t1['file'])
        custom_part_summary.append({
            'name': cp['name'],
            'primitive_count': len([l for l in cp['lines'] if parse_type1(l)]),
            'primitives_used': list(set(primitives))[:20],
        })

    return {
        'set': set_label,
        'mpd_path': mpd_path,
        'sub_model_count': len(main_blocks),
        'main_block_lines': len(master_block['lines']) if master_block else 0,
        'master_piece_count': len(master_pieces),
        'all_type1_count': len(all_instances),
        'step_count': len(steps_in_master),
        'steps_distribution': dict(Counter(steps_in_master)),
        'pieces_per_step_stats': {
            'mean': (sum(steps_in_master)/len(steps_in_master)) if steps_in_master else 0,
            'min': min(steps_in_master) if steps_in_master else 0,
            'max': max(steps_in_master) if steps_in_master else 0,
        },
        'custom_part_count': len(custom_parts),
        'top_pieces': file_counter.most_common(30),
        'color_distribution_top10': color_counter.most_common(10),
        'unique_colors': len(color_counter),
        'unique_files': len(file_counter),
        'matrix_distribution_top10': [
            (list(m), c) for m, c in matrix_counter.most_common(10)
        ],
        'bbox': bbox,
        'y_layer_distribution_top20': y_values.most_common(20),
        'sub_builds_piece_count': len(sub_build_pieces),
        'custom_part_summary': custom_part_summary[:10],
    }


if __name__ == '__main__':
    out = {
        '10252_VW_Beetle': analyze_set('corpus/10252-1.mpd', '10252', '10252 Volkswagen Beetle'),
        '10218_PetShop':   analyze_set('corpus/10218-1.mpd', '10218', '10218 Pet Shop'),
    }
    Path('analysis').mkdir(exist_ok=True)
    Path('analysis/raw_stats.json').write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk not in ('custom_part_summary',)} for k, v in out.items()}, indent=2))
