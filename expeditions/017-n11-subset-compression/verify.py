#!/usr/bin/env python3
"""Exact removal of redundant partition labels in the fixed n11 witness.

This verifies the SAME probability measure on polynomial objects, not a new
optimization or a Lean theorem. Standard library; all checks survive -O.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial
from pathlib import Path
import argparse
import hashlib
import json

N = 11
ALL = (1 << N) - 1
PAIRS = tuple(combinations(range(N), 2))
EDGE = {p: k for k, p in enumerate(PAIRS)}
TARGET = [int(x.bit_count() % 3 == 0) for x in range(1 << N)]
FEATURE = [sum(1 << k for k, (i,j) in enumerate(PAIRS)
               if x >> i & 1 and x >> j & 1) for x in range(1 << N)]
SOURCE_BLOB = '2fed5a9a274f358deedf59879f4ba1160eb3214f'


def require(ok, why):
    if not ok:
        raise ValueError(why)


def clique(subset):
    return sum(1 << EDGE[(i,j)] for i,j in combinations(sorted(subset), 2))


def polynomial(row, x):
    c, linear, quadratic = row
    return (c + (linear & x).bit_count() + (quadratic & FEATURE[x]).bit_count()) % 2


def block_row(partition, code):
    c, linear, quadratic = code & 1, 0, 0
    for k, part in enumerate(partition):
        if code >> (1+k) & 1:
            linear |= sum(1 << i for i in part)
        if code >> (4+k) & 1:
            quadratic |= clique(part)
    for k, (i,j) in enumerate(combinations(range(3), 2)):
        if code >> (7+k) & 1:
            quadratic |= sum(1 << EDGE[tuple(sorted((a,b)))]
                             for a in partition[i] for b in partition[j])
    return c, linear, quadratic


def partitions(shape):
    a,b,_ = shape
    for aa in combinations(range(N), a):
        rest = tuple(i for i in range(N) if i not in aa)
        for bb in combinations(rest,b):
            yield aa, bb, tuple(i for i in rest if i not in bb)


def canonical_json(obj):
    return json.dumps(obj, separators=(',', ':'), sort_keys=True).encode()


def build_support():
    support = {(0,0,0): 165}
    descriptors = []
    for a, shift, mass in [(8,0,4),(7,1,1)]:
        for subset in combinations(range(N),a):
            mask = sum(1 << i for i in subset)
            row = (1, ALL if shift == 0 else ALL ^ mask, clique(subset))
            require(row not in support, 'unexpected duplicate polynomial')
            support[row] = mass
            descriptors.append((row,mask,shift))
    return support, descriptors


def score_support(support):
    return [sum(m for row,m in support.items() if polynomial(row,x)==TARGET[x])
            for x in range(1 << N)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--write-support', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    source = root / 'expeditions/015-n11-mixture/compact-certificate.json'
    raw = source.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    require(blob == SOURCE_BLOB, 'source certificate changed; reconcile provenance')
    d = json.loads(raw)
    require(d['probability_denominator']==7 and
            [(s['blocks'],s['code'],s['weight']) for s in d['seeds']] ==
            [([9,1,1],0,1),([8,2,1],31,4),([7,3,1],29,2)], 'wrong source model')
    support, descriptors = build_support()
    require(len(support)==496 and sum(support.values())==1155, 'normalization/support mismatch')
    original = defaultdict(F)
    fibers = []
    raw_count = 0
    for seed in d['seeds']:
        counts = Counter(block_row(p,seed['code']) for p in partitions(seed['blocks']))
        orbit = sum(counts.values())
        raw_count += orbit
        fibers.append({'indexed':orbit,'distinct':len(counts),
                       'fiber_multiplicities':sorted(set(counts.values()))})
        for row, multiplicity in counts.items():
            original[row] += F(seed['weight']*multiplicity,7*orbit)
    require(raw_count==1925 and dict(original)=={r:F(m,1155) for r,m in support.items()},
            'not the same measure on polynomial coefficient rows')
    require(fibers == [{'indexed':110,'distinct':1,'fiber_multiplicities':[110]},
                       {'indexed':495,'distinct':165,'fiber_multiplicities':[3]},
                       {'indexed':1320,'distinct':330,'fiber_multiplicities':[4]}],
            'unexpected quotient fibers')
    # Separate algebraic description: q = 1 + weight(x) + choose(k+shift,2) in GF(2).
    evaluations = 0
    for row, mask, shift in descriptors:
        for x in range(1 << N):
            k = (mask & x).bit_count()
            require(polynomial(row,x) == (1+x.bit_count()+comb(k+shift,2))%2,
                    'explicit polynomial and subset-count formula disagree')
            evaluations += 1
    point = score_support(support)
    by_layer = []
    hyper_counts = []
    for w in range(N+1):
        counts = []
        for a, shift in [(8,0),(7,1)]:
            total = 0
            for k in range(a+1):
                if 0 <= w-k <= N-a and (1+w+comb(k+shift,2))%2 == int(w%3==0):
                    total += comb(a,k)*comb(N-a,w-k)
            counts.append(total)
        expected = F(int(w%3!=0),7) + F(4*counts[0]+2*counts[1],7*comb(N,w))
        observed = {F(point[x],1155) for x in range(1 << N) if x.bit_count()==w}
        require(observed=={expected}, 'hypergeometric and full pointwise scores differ')
        by_layer.append(expected); hyper_counts.append(counts)
    require(min(by_layer)==F(158,231)>F(2,3), 'upper threshold changed')
    # Recheck the unchanged dual on every affine coefficient row.
    mass = [(x,15 if x.bit_count()==1 else 1) for x in range(1 << N) if x.bit_count() in (1,3)]
    scores = [sum(m for x,m in mass if (c^((a&x).bit_count()%2))==TARGET[x])
              for c in (0,1) for a in range(1 << N)]
    require(sum(m for _,m in mass)==330 and len(scores)==4096 and max(scores)==207,
            'unchanged affine lower obstruction failed')
    # This diagnostic deliberately tries invalid quotient/normalization shortcuts.
    rejected = []
    uniform = {r:F(1,len(support)) for r in support}
    require(uniform != original, 'uniformization unexpectedly preserved measure')
    uniform_point = score_support({r:1 for r in support})
    require(min(uniform_point)*3 < 2*len(support), 'uniformization not refuted')
    rejected.append('uniformize_distinct_support')
    lost_fibers = {}
    for seed in d['seeds']:
        rows = list(partitions(seed['blocks']))
        for p in rows:
            lost_fibers[block_row(p,seed['code'])] = F(seed['weight'],7*len(rows))
    require(sum(lost_fibers.values()) != 1, 'discarding duplicates without mass aggregation escaped')
    rejected.append('discard_duplicate_mass')
    wrong = dict(support); r = next(r for r in wrong if r != (0,0,0)); m = wrong.pop(r)
    q = (r[0]^1,r[1],r[2]); wrong[q] = wrong.get(q,0)+m
    require(wrong != support and score_support(wrong) != point, 'coefficient mutation escaped')
    rejected.append('flip_coefficient')
    raw_rows = [(0,0,0),(1,ALL,clique(range(8))),(1,ALL ^ ((1<<7)-1),clique(range(7)))]
    raw_point = [sum(m for r,m in zip(raw_rows,[1,4,2]) if polynomial(r,x)==TARGET[x]) for x in range(1<<N)]
    require(min(raw_point)*3<14, 'raw unsymmetrized shortcut not refuted')
    rejected.append('omit_symmetrization')
    rows = [list(r)+[m] for r,m in sorted(support.items())]
    encoded = canonical_json(rows)
    if args.write_support:
        args.write_support.write_text(encoded.decode()+'\n')
    result = {'status':'exact finite measure equivalence, not a Lean theorem',
              'n':N,'source_git_blob':blob,'old_indexed_support':raw_count,
              'distinct_support':len(support),'denominator':1155,
              'support_sha256':hashlib.sha256(encoded).hexdigest(),
              'point_scores_sha256':hashlib.sha256(canonical_json(point)).hexdigest(),
              'fibers':fibers,'independent_formula_evaluations':evaluations,
              'upper_by_layer':list(map(str,by_layer)), 'upper_minimum':str(min(by_layer)),
              'upper_margin':str(min(by_layer)-F(2,3)), 'hypergeometric_seed_good_counts':hyper_counts,
              'affine_rows':len(scores),'affine_bound':'69/110',
              'rejected_shortcuts':rejected,'uniformized_minimum':str(F(min(uniform_point),496)),
              'raw_unsymmetrized_minimum':str(F(min(raw_point),7)),
              'raw_counterexample_mask':raw_point.index(min(raw_point))}
    print(json.dumps(result,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
