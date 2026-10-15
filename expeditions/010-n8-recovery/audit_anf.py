#!/usr/bin/env python3
"""Independent integer audit by subset zeta transform and Walsh dual transform.

Does not import the optimizer, group construction or tuple-evaluation checker.
These are finite same-author checks, not Lean or independent human review.
"""
import argparse
from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(obj):
    return sha256(json.dumps(obj, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def verify(data):
    require(data['n'] == 8 and data['field'] == 'GF(2)' and data['degree_bound'] == 2,
            'incorrect mathematical scope')
    require(data['target'] == 'weight divisible by 3' and data['success_threshold'] == '2/3',
            'incorrect target or threshold')
    D, rows = data['denominator'], data['rows_c_a_b_tickets']
    require(type(D) is int and D > 0 and len(rows) > 0, 'invalid distribution')
    pairs = tuple(combinations(range(8), 2))
    good = [0] * 256
    seen = set()
    total = 0
    for row in rows:
        require(len(row) == 4 and all(type(v) is int for v in row), 'noninteger row')
        c, a, b, t = row
        require(c in (0, 1) and 0 <= a < 256 and 0 <= b < 2**28 and t > 0,
                'invalid polynomial or probability')
        require((c, a, b) not in seen, 'duplicate row')
        seen.add((c, a, b))
        total += t
        coeff = [0] * 256
        coeff[0] = c
        for i in range(8):
            coeff[1 << i] = (a >> i) & 1
        for k, (i, j) in enumerate(pairs):
            coeff[(1 << i) | (1 << j)] = (b >> k) & 1
        require(all(s.bit_count() <= 2 for s, v in enumerate(coeff) if v), 'degree failure')
        values = coeff[:]
        for i in range(8):
            for x in range(256):
                if x & (1 << i):
                    values[x] ^= values[x ^ (1 << i)]
        for x, v in enumerate(values):
            if v == int(x.bit_count() % 3 == 0):
                good[x] += t
        # The same involution must recover every original ANF coefficient.
        for i in range(8):
            for x in range(256):
                if x & (1 << i):
                    values[x] ^= values[x ^ (1 << i)]
        require(values == coeff, 'ANF reconstruction failed')
    require(total == D and min(good) * 3 >= 2 * D, 'pointwise or normalization failure')
    masses = [7 if x.bit_count() == 1 else 1 if x.bit_count() == 3 else 0 for x in range(256)]
    W = [m * (-1 if x.bit_count() % 3 == 0 else 1) for x, m in enumerate(masses)]
    width = 1
    while width < 256:
        for start in range(0, 256, 2 * width):
            for j in range(start, start + width):
                a, b = W[j], W[j + width]
                W[j], W[j + width] = a + b, a - b
        width *= 2
    require(sum(masses) == 112 and max(abs(w) for w in W) == 32, 'Walsh obstruction failure')
    scores = [(112 + sign * w) // 2 for sign in (1, -1) for w in W]
    require(max(scores) == 72 and 3 * 72 < 2 * 112, 'incorrect dual gap')
    ratios = [str(Fraction(t, D)) for t in good]
    return {'rows': len(rows), 'denominator': D, 'all_inputs': 256,
            'minimum_success': str(Fraction(min(good), D)),
            'tight_inputs': sum(3 * t == 2 * D for t in good),
            'pointwise_success_sha256': digest(ratios),
            'integer_success_numerators': good,
            'affine_rows_from_walsh': 512, 'maximum_affine_score': '9/14',
            'coefficient_rows_sha256': digest(rows)}


def controls(data):
    edits = [
        ('duplicate_row', lambda d: d['rows_c_a_b_tickets'].append(d['rows_c_a_b_tickets'][0][:])),
        ('zero_ticket', lambda d: d['rows_c_a_b_tickets'][0].__setitem__(3, 0)),
        ('float_ticket', lambda d: d['rows_c_a_b_tickets'][0].__setitem__(3, 1.0)),
        ('wrong_target', lambda d: d.__setitem__('target', 'weight not divisible by 3')),
        ('wrong_arity', lambda d: d.__setitem__('n', 9)),
        ('bad_high_degree_mask', lambda d: d['rows_c_a_b_tickets'][0].__setitem__(2, 2**28))]
    rejected = []
    for name, edit in edits:
        damaged = deepcopy(data)
        edit(damaged)
        try:
            verify(damaged)
        except ValueError:
            rejected.append(name)
        else:
            raise ValueError('accepted mutation: ' + name)
    return rejected


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    args = parser.parse_args()
    data = json.loads(args.certificate.read_text())
    print(json.dumps({'result': verify(data), 'mutations_rejected': controls(data)}, indent=2))
