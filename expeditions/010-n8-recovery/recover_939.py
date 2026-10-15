#!/usr/bin/env python3
"""Recover the prior unsaved 939-row witness, with exact coefficient provenance.

No optimizer. Binary affine maps on eight labels are enumerated explicitly;
all correctness guarantees must still be checked by verify_compact.py.
"""
from collections import Counter
from itertools import combinations, product
import hashlib
import json

PAIRS = tuple(combinations(range(8), 2))
PAIR_INDEX = {p: i for i, p in enumerate(PAIRS)}
LABELS = (0, 1, 2, 3, 4, 5, 7, 6)
SEEDS = ((0, 0, 268435455, 1), (0, 166, 191494995, 3),
         (1, 155, 254268221, 4), (1, 127, 66817983, 4))
EXPECTED_ROWS_SHA256 = 'ffd64b510a09c110fd1843e988e0b0948740319b6a03ea78a487f8223d3da666'


def require(ok, message):
    if not ok:
        raise ValueError(message)


def rename(row, p):
    c, a, b = row
    aa = sum(1 << p[i] for i in range(8) if (a >> i) & 1)
    bb = sum(1 << PAIR_INDEX[tuple(sorted((p[i], p[j])))]
             for k, (i, j) in enumerate(PAIRS) if (b >> k) & 1)
    return c, aa, bb


def recover():
    group = set()
    for columns in product(range(1, 8), repeat=3):
        linear = tuple((columns[0] if x & 1 else 0) ^
                       (columns[1] if x & 2 else 0) ^
                       (columns[2] if x & 4 else 0) for x in range(8))
        if len(set(linear)) != 8:
            continue
        for t in range(8):
            group.add(tuple(LABELS[linear[LABELS[i]] ^ t] for i in range(8)))
    require(len(group) == 1344, 'affine-map enumeration changed')
    masses = Counter()
    for p in sorted(group):
        for c, a, b, t in SEEDS:
            masses[rename((c, a, b), p)] += t
    require(len(masses) == 939, 'recovered support differs')
    require(all(t % 8 == 0 for t in masses.values()), 'ticket reduction differs')
    rows = [list(row) + [t // 8] for row, t in sorted(masses.items())]
    digest = hashlib.sha256(json.dumps(rows, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    require(digest == EXPECTED_ROWS_SHA256, 'not the prior coefficient witness')
    require(sum(r[3] for r in rows) == 2016, 'normalization differs')
    return dict(n=8, field='GF(2)', target='weight divisible by 3', degree_bound=2,
                success_threshold='2/3', denominator=2016, rows_c_a_b_tickets=rows)


if __name__ == '__main__':
    print(json.dumps(recover(), indent=2))
