#!/usr/bin/env python3
"""Finite continuation only: independently sampled inner/root hash matrices.
Reuses the already checked sparse arithmetic, not an independent author/kernel.
Never substitutes this bounded calculation for the generic root-budget proof.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
import json
from check_slots import Gate, one, variable, mul, degree, peval, polys, values, bit_gate, require


def matrices(K, r):
    return tuple(product(tuple(product((0, 1), repeat=K)), repeat=r))


def top_poly(n, root, table, B):
    O = one(n)
    children = []
    for w in root.refs:
        p = (O if root.op == 'and' else frozenset()) if w is None else (
            variable(n, w[1]) if w[0] == 'i' else table[w[1]])
        children.append(O ^ p if root.op == 'and' else p)
    out = O
    for row in B:
        h = frozenset()
        for a, p in zip(row, children):
            if a:
                h ^= p
        out = mul(out, O ^ h)
    return out if root.op == 'and' else O ^ out


def read_args(root, x, chronological):
    return tuple(int(root.op == 'and') if w is None else (
        x[w[1]] if w[0] == 'i' else chronological[-1-w[1]]) for w in root.refs)


def inner_bad(gates, x, true, A):
    for j, g in enumerate(gates):
        z = read_args(g, x, true[:j])
        if bit_gate(g, z, A) != true[j]:
            return True
    return False


def check_case(n, K, inner, root, r, t, counts):
    require(root.op in ('or', 'and') and len(root.refs) == K, 'nonlinear root required')
    require(r >= 1 and t >= 1, 'positive sample counts')
    S = sum(g.op in ('or', 'and') for g in inner)
    xs = tuple(product((0, 1), repeat=n))
    true = [values(inner, x) for x in xs]
    As, Bs = matrices(K, r), matrices(K, t)
    fail = [0] * len(xs)
    counts['parameter_cases'] += 1
    for A in As:
        table, depths = polys(n, inner, A)
        H = max((0 if w is None or w[0] == 'i' else depths[w[1]] for w in root.refs), default=0)
        for B in Bs:
            p = top_poly(n, root, table, B)
            require(degree(p) <= t * r**H, 'actual composed root degree')
            counts['matrix_pairs'] += 1
            counts['degree_checks'] += 1
            for i, x in enumerate(xs):
                actual = bit_gate(root, read_args(root, x, values(inner, x, A)), B)
                expected = bit_gate(root, read_args(root, x, true[i]))
                top_bad = bit_gate(root, read_args(root, x, true[i]), B) != expected
                require(peval(p, x) == actual, 'actual polynomial/Boolean mismatch')
                wrong = actual != expected
                require(not wrong or inner_bad(inner, x, true[i], A) or top_bad,
                        'true-child event union inclusion')
                fail[i] += wrong
                counts['pointwise_evaluations'] += 1
    space = len(As) * len(Bs)
    for f in fail:
        require(Fraction(f, space) <= Fraction(S, 2**r) + Fraction(1, 2**t), 'root error budget')
        counts['pointwise_error_bounds'] += 1
        if t == 2 and 12*S <= 2**r:
            require(Fraction(f, space) <= Fraction(1, 3), 'one-third guarantee')
            counts['one_third_bounds'] += 1


def main():
    i0, i1 = ('i', 0), ('i', 1)
    g0, g1 = ('g', 0), ('g', 1)
    cases = (
        (0, 0, (), Gate('and', ())),
        (0, 0, (), Gate('or', ())),
        (2, 2, (), Gate('or', (i0, i1))),
        (2, 2, (), Gate('and', (i0, None))),
        (2, 2, (Gate('or', (i0, i1)),), Gate('and', (g0, g0))),
        (2, 2, (Gate('and', (i0, i1)), Gate('not', (g0,))), Gate('or', (g0, g1))),
        (2, 2, (Gate('or', (i0, i0)), Gate('xor', (g0, i0))), Gate('and', (g0, g1))),
        (2, 2, (Gate('and', (None, None)),), Gate('or', (g0, None))),
    )
    counts = Counter()
    for case in cases:
        for r in (1, 2):
            for t in (1, 2):
                check_case(*case, r, t, counts)
    # A nontrivial inner error budget: S=1,r=4,t=2 satisfies12*S<=2^r.
    for case in cases[4:]:
        check_case(*case, 4, 2, counts)
    print(json.dumps({'status': 'PASS', 'scope': 'local finite continuation; not CI or generic proof',
        'independence': 'explicit Cartesian product of inner and root matrix spaces',
        'authorship': 'same author; sparse arithmetic reused from check_slots.py',
        'circuits': len(cases), 'counts': dict(counts)}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
