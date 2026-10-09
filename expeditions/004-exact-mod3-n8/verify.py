#!/usr/bin/env python3
"""Exact n=8 certificate; Python standard library. No optimizer is trusted.

Run `python3 verify.py --permutations` for a second evaluator and literal
all-permutation, all-input audit. Checks remain active under python -O.
The formal group-action and convexity arguments are in conclusion.md.
"""
from __future__ import annotations
import argparse
from copy import deepcopy
from fractions import Fraction as Q
from itertools import combinations, permutations
import json
from math import comb, factorial
from pathlib import Path

N = 8
PAIRS = tuple(combinations(range(N), 2))
SIZES = tuple(comb(N, w) for w in range(N + 1))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def evaluate(row: dict, x: int) -> int:
    value = row['c'] ^ ((row['a'] & x).bit_count() & 1)
    for k, (i, j) in enumerate(PAIRS):
        value ^= ((row['b'] >> k) & 1) & ((x >> i) & 1) & ((x >> j) & 1)
    return value


def verify(data: dict) -> tuple[list[Q], list[list[int]]]:
    require(data['n'] == 8 and data['field'] == 'GF(2)', 'wrong model')
    require(data['target'] == 'weight divisible by 3', 'wrong target')
    require(Q(data['threshold']) == Q(2, 3), 'wrong error threshold')
    q = list(map(Q, data['lower_layer_mass']))
    require(len(q) == 9 and all(v >= 0 for v in q) and sum(q) == 1, 'bad input distribution')
    lower = []
    for c in (0, 1):
        for a in range(256):
            good = [0] * 9
            for x in range(256):
                w = x.bit_count()
                good[w] += (c ^ ((a & x).bit_count() & 1)) == int(w % 3 == 0)
            lower.append(sum(q[w] * Q(good[w], SIZES[w]) for w in range(9)))
    require(len(lower) == 512, 'affine coverage failure')
    require(max(lower) == Q(data['lower_maximum']) == Q(9, 14), 'lower mismatch')
    require(max(lower) < Q(2, 3), 'not a separating distribution')
    # Independent affine calculation by hypergeometric counting, grouped by |a|.
    for k in range(9):
        good3 = sum(comb(k, j) * comb(8-k, 3-j)
                    for j in (1, 3) if j <= k and 0 <= 3-j <= 8-k)
        mean = Q(8-k, 16) + Q(good3, 112)
        require(lower[(1 << k)-1] == mean and lower[256+(1 << k)-1] == 1-mean,
                'independent affine formula mismatch')
    weights = [Q(row['weight']) for row in data['upper']]
    require(len(weights) == 4 and all(w >= 0 for w in weights) and sum(weights) == 1,
            'invalid polynomial distribution')
    tables = []
    for row in data['upper']:
        require(row['c'] in (0, 1) and 0 <= row['a'] < 256 and 0 <= row['b'] < (1 << 28),
                'coefficient outside degree-two encoding')
        table = [evaluate(row, x) for x in range(256)]
        good = [sum(table[x] == int(w % 3 == 0) for x in range(256) if x.bit_count() == w)
                for w in range(9)]
        require(good == row['good'], 'truth table does not match certificate')
        tables.append(table)
    success = [sum(weights[r] * Q(data['upper'][r]['good'][w], SIZES[w]) for r in range(4))
               for w in range(9)]
    require(success == list(map(Q, data['upper_layer_success'])), 'rational mixture mismatch')
    require(min(success) >= Q(2, 3), 'upper threshold failure')
    return success, tables


def permutation_audit(data: dict, success: list[Q], reference: list[list[int]]) -> None:
    # Independent evaluator: tuples, selected linear coordinates and explicit edges.
    # It shares certificate data but neither bit-parity evaluation nor layer counting.
    direct = []
    for row in data['upper']:
        linear = [i for i in range(8) if row['a'] // (2**i) % 2]
        edges = [pair for k, pair in enumerate(PAIRS) if row['b'] // (2**k) % 2]
        table = []
        for x in range(256):
            bits = tuple(x // (2**i) % 2 for i in range(8))
            table.append((row['c'] + sum(bits[i] for i in linear)
                          + sum(bits[i]*bits[j] for i,j in edges)) % 2)
        direct.append(table)
    require(direct == reference, 'second polynomial evaluator disagrees')
    tally = [[0] * 256 for _ in range(4)]
    targets = [int(sum(x // (2**i) % 2 for i in range(8)) % 3 == 0) for x in range(256)]
    predecessor = [(x & (x-1), (x & -x).bit_length()-1) for x in range(1, 256)]
    total = 0
    for perm in permutations(range(8)):
        image = [0] * 256
        for x, (previous, bit) in enumerate(predecessor, 1):
            image[x] = image[previous] + 2**perm[bit]
        for r, table in enumerate(direct):
            for x, y in enumerate(image):
                tally[r][x] += table[y] == targets[x]
        total += 1
    require(total == factorial(8), 'permutation coverage failure')
    for x in range(256):
        actual = sum(Q(data['upper'][r]['weight']) * Q(tally[r][x], total) for r in range(4))
        require(actual == success[x.bit_count()] and actual >= Q(2, 3),
                f'pointwise permutation failure at {x}')
    print('PERMUTATIONS: 40320 permutations x 256 fixed inputs x 4 representatives: PASS')


def negative_controls(data: dict, tables: list[list[int]]) -> None:
    # Each malformed certificate must fail the normal validator (no assert shortcuts).
    bad = deepcopy(data); bad['upper'][2]['c'] ^= 1
    bad_weight = deepcopy(data); bad_weight['upper'][0]['weight'] = '-1/12'
    bad_degree = deepcopy(data); bad_degree['upper'][0]['b'] |= 1 << 28
    bad_target = deepcopy(data); bad_target['target'] = 'weight not divisible by 3'
    bad_lower = deepcopy(data); bad_lower['lower_layer_mass'] = ['1'] + ['0']*8
    for label, item in [('flipped constant', bad), ('negative weight', bad_weight),
                        ('out-of-range monomial', bad_degree), ('wrong target', bad_target),
                        ('invalid lower witness', bad_lower)]:
        try:
            verify(item)
        except ValueError:
            print(f'NEGATIVE CONTROL: {label}: rejected')
        else:
            raise ValueError(f'accepted negative control: {label}')
    raw = [sum(Q(row['weight']) * (tables[r][x] == int(x.bit_count()%3 == 0))
               for r, row in enumerate(data['upper'])) for x in range(256)]
    require(min(raw) < Q(2,3), 'unsymmetrized control unexpectedly passed')
    print(f'NEGATIVE CONTROL: omit permutation randomization: minimum={min(raw)} < 2/3')


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--permutations', action='store_true')
    args = parser.parse_args()
    data = json.loads(Path(__file__).with_name('certificate.json').read_text())
    success, tables = verify(data)
    print('LOWER: all 512 affine polynomials; maximum=9/14 < 2/3')
    print('UPPER: weights=1/12,1/4,1/3,1/3; layer success=' + ','.join(map(str,success)))
    if args.permutations:
        permutation_audit(data, success, tables)
    negative_controls(data, tables)
    print('PASS: finite n=8 certificate for pdeg_(1/3)^GF(2)(MOD_3^8)=2; no novelty or asymptotic claim')


if __name__ == '__main__':
    main()
