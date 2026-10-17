#!/usr/bin/env python3
"""Independent finite n10 statement/encoding audit; never a Lean proof.

Recover ANF coefficients using value queries at weights zero, one and two,
then check every value against block-parity evaluation and a full Mobius
transform. Compare the recovered rows with the actual Lean literal table.
Standard library only; explicit exceptions also execute under python -O.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import re

N = 10
PAIRS = tuple(combinations(range(N), 2))

def require(ok, why):
    if not ok:
        raise ValueError(why)

def block_value(seed, x):
    counts, offset = [], 0
    for size in seed['blocks']:
        counts.append(sum((x >> i) & 1 for i in range(offset, offset + size)))
        offset += size
    features = [1] + counts + [comb(k, 2) for k in counts]
    features += [counts[i] * counts[j] for i, j in combinations(range(3), 2)]
    return sum(v for bit, v in enumerate(features) if (seed['code'] >> bit) & 1) % 2

def recover_row(seed):
    c = block_value(seed, 0)
    linear = [block_value(seed, 1 << i) ^ c for i in range(N)]
    quad = [block_value(seed, (1 << i) | (1 << j)) ^ c ^ linear[i] ^ linear[j]
            for i, j in PAIRS]
    return c, sum(v << i for i, v in enumerate(linear)), sum(v << i for i, v in enumerate(quad))

def row_value(row, x):
    c, linear, quad = row
    return (c + (linear & x).bit_count() + sum(((quad >> k) & 1) *
            ((x >> i) & 1) * ((x >> j) & 1) for k, (i, j) in enumerate(PAIRS))) % 2

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--skip-lean-source', action='store_true')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    certificate = root / 'expeditions/013-n10-mixture/certificate.json'
    d = json.loads(certificate.read_text())
    require(d['n'] == N and d['field'] == 'GF(2)' and d['error'] == '1/3', 'wrong model')
    require(d['target'] == 'one iff Hamming weight divisible by three', 'wrong target')
    require(len(d['seeds']) == 8 and d['probability_denominator'] == 100, 'wrong mixture')
    require(sum(s['weight'] for s in d['seeds']) == 100, 'unnormalized')
    target = [int(x.bit_count() % 3 == 0) for x in range(1 << N)]
    rows, layers, values = [], [], []
    for seed in d['seeds']:
        require(len(seed['blocks']) == 3 and sum(seed['blocks']) == N
                and all(s > 0 for s in seed['blocks']) and 0 <= seed['code'] < 1024,
                'bad block shape or code')
        row = recover_row(seed)
        val = [block_value(seed, x) for x in range(1 << N)]
        require(val == [row_value(row, x) for x in range(1 << N)], 'ANF mismatch')
        anf = val[:]
        for i in range(N):
            for x in range(1 << N):
                if (x >> i) & 1:
                    anf[x] ^= anf[x ^ (1 << i)]
        require(all(x.bit_count() <= 2 for x, a in enumerate(anf) if a), 'degree exceeds two')
        count = [sum(val[x] == target[x] for x in range(1 << N) if x.bit_count() == w)
                 for w in range(N + 1)]
        require(count == seed['good'], 'layer-count mismatch')
        rows.append(row); layers.append(count); values.append(val)
    triple_weights = [3 * s['weight'] for s in d['seeds']]
    layer_tickets = [sum(t * g[w] for t, g in zip(triple_weights, layers)) for w in range(N + 1)]
    successes = [F(v, 300 * comb(N, w)) for w, v in enumerate(layer_tickets)]
    require(min(successes) == F(2123, 3000) and all(v > F(2, 3) for v in successes), 'upper failed')
    raw = [sum(t for t, val in zip(triple_weights, values) if val[x] == target[x])
           for x in range(1 << N)]
    raw_min = min(raw); raw_input = raw.index(raw_min)
    require(raw_min < 200, 'missing raw-mixture counterexample')
    mass = [12 if x.bit_count() == 1 else 1 if x.bit_count() == 3 else 0 for x in range(1 << N)]
    scores = [[sum(m for x, m in enumerate(mass)
                  if (c ^ ((a & x).bit_count() % 2)) == target[x])
               for a in range(1 << N)] for c in (0, 1)]
    require(sum(mass) == d['dual_denominator'] == 240 and
            max(map(max, scores)) == d['affine_upper_score'] == 152 and
            d['dual_mass_by_weight'] == {'1': 12, '3': 1}, 'lower failed')
    canonical = [[scores[c][(1 << w) - 1] for w in range(N + 1)] for c in (0, 1)]
    for c in (0, 1):
        for a in range(1 << N):
            require(scores[c][a] == canonical[c][a.bit_count()], 'coefficient-orbit coverage failed')
    for w in range(N + 1):
        odd = sum(comb(w, k) * comb(N - w, 3 - k) for k in (1, 3)
                  if k <= w and 0 <= 3 - k <= N - w)
        require(canonical[0][w] == 12 * (N - w) + odd, 'hypergeometric formula failed')
    controls = []
    for r, row in enumerate(rows):
        for bit in range(1 + N + len(PAIRS)):
            q = list(row)
            if bit == 0: q[0] ^= 1
            elif bit <= N: q[1] ^= 1 << (bit - 1)
            else: q[2] ^= 1 << (bit - 1 - N)
            require(any(row_value(q, x) != values[r][x] for x in range(1 << N)), 'mutation escaped')
            controls.append([r, bit])
    lean_path = root / 'formal/PvsNPCartography/Mod3TenDegree.lean'
    lean_hash = None
    if not args.skip_lean_source:
        source = lean_path.read_text()
        def section(a, b):
            return source.split(a, 1)[1].split(b, 1)[0]
        actual_pairs = [tuple(map(int, z)) for z in re.findall(r'\((\d+),\s*(\d+)\)', section('def pairs', 'def rows'))]
        actual_rows = [tuple(map(int, z)) for z in re.findall(r'\((\d+),\s*(\d+),\s*(\d+)\)', section('def rows', 'def weights'))]
        actual_weights = list(map(int, re.search(r'!\[([^]]+)\]', section('def weights', 'def tickets')).group(1).split(',')))
        require(actual_pairs == list(PAIRS), 'Lean pair order mismatch')
        require(actual_rows == rows, 'Lean row data mismatch')
        require(actual_weights == triple_weights, 'Lean weights mismatch')
        actual_layers = list(map(int, re.search(r'!\[([^]]+)\]', section('def layerTickets', 'theorem layer_tickets_exact')).group(1).split(',')))
        require(actual_layers == layer_tickets, 'Lean layer table mismatch')
        require(not re.search(r'\b(sorry|admit|native_decide)\b', source), 'placeholder/unchecked decision')
        lean_hash = hashlib.sha256(source.encode()).hexdigest()
    result = {'state': 'exact finite audit, not formal execution', 'inputs': 1024,
              'rows': rows, 'triple_weights': triple_weights, 'layer_tickets': layer_tickets,
              'upper_by_layer': list(map(str, successes)), 'upper_minimum': str(min(successes)),
              'affine_rows': 2048, 'canonical_affine_scores': canonical,
              'affine_maximum': '19/30', 'raw_minimum': str(F(raw_min, 300)),
              'raw_counterexample_mask': raw_input, 'raw_counterexample_little_endian': [(raw_input >> i) & 1 for i in range(N)],
              'single_coefficient_mutations_detected': len(controls), 'lean_source_sha256': lean_hash}
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == '__main__':
    main()
