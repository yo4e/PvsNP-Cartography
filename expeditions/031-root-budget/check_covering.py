#!/usr/bin/env python3
"""Finite Hamming-cover continuation, not pointwise-mixture classification."""
from collections import Counter
from math import comb
import json


def require(p, text):
    if not p:
        raise RuntimeError(text)


def check(n, d):
    N = 1 << n
    supports = [s for s in range(N) if s.bit_count() <= d]
    # Monomial evaluations, with inputs encoded by their set of 1-coordinates.
    monos = [sum(1 << x for x in range(N) if x & s == s) for s in supports]
    rows = [0]
    for a in monos:
        rows += [v ^ a for v in rows]
    M = sum(comb(n, j) for j in range(min(d, n) + 1))
    require(len(set(rows)) == 1 << M, 'multilinear evaluation injectivity')
    hist = Counter(min((f ^ p).bit_count() for p in rows) for f in range(1 << N))
    radius = N // 3
    covered = sum(c for dist, c in hist.items() if dist <= radius)
    volume = sum(comb(N, j) for j in range(radius + 1))
    require(covered <= (1 << M) * volume, 'union volume bound')
    return dict(n=n, d=d, truth_table_length=N, dimension=M, rows=len(rows),
                radius=radius, actual_covered=covered, total_targets=1 << N,
                union_bound=(1 << M)*volume, distance_histogram=dict(sorted(hist.items())))


def main():
    out = [check(n, d) for n in range(4) for d in range(min(n, 2)+1)]
    out += [check(4, 0), check(4, 1)]
    # AND on two inputs has truth table 0001, distance 1 from the zero constant.
    # A pointwise constant mixture needs both p>=2/3 and 1-p>=2/3: impossible.
    require((1 << 3).bit_count() == 1 and 3*1 <= 4, 'average-only witness')
    print(json.dumps(dict(status='PASS', scope='finite covering counts, not a Lean proof or pdeg classification',
        cases=out, false_converse=dict(n=2,d=0,target='AND',zero_constant_agreement='3/4',
        pointwise_feasible=False,reason='constant-one mass would need >=2/3 and <=1/3')), indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
