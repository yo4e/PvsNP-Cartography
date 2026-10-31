#!/usr/bin/env python3
"""Exact finite controls, not a generic proof or independent semantic review.
Two same-author implementations: unreduced sparse GF(2) polynomials in a
newest-first table, and Boolean gates in a chronological table. Python >=3.10.
All checks remain enabled with python -O. No third-party dependencies.
"""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from itertools import product
import json

Wire = tuple[str, int] | None
Poly = frozenset[tuple[int, ...]]

@dataclass(frozen=True)
class Gate:
    op: str
    refs: tuple[Wire, ...] = ()
    bit: int = 0

def require(p: bool, text: str) -> None:
    if not p:
        raise RuntimeError(text)

def one(n: int) -> Poly:
    return frozenset({(0,) * n})

def var(n: int, j: int) -> Poly:
    return frozenset({tuple(int(i == j) for i in range(n))})

@lru_cache(maxsize=32768)
def mul(a: Poly, b: Poly) -> Poly:
    out: set[tuple[int, ...]] = set()
    for u in a:
        for v in b:
            e = tuple(x + y for x, y in zip(u, v))
            if e in out:
                out.remove(e)
            else:
                out.add(e)
    return frozenset(out)

def degree(p: Poly) -> int:
    return max(map(sum, p), default=0)

def peval(p: Poly, x: tuple[int, ...]) -> int:
    return sum(all(e == 0 or b == 1 for e, b in zip(m, x)) for m in p) % 2

@lru_cache(maxsize=None)
def matrices(K: int, r: int) -> tuple:
    return tuple(product(tuple(product((0, 1), repeat=K)), repeat=r))

def bitgate(g: Gate, z: tuple[int, ...], A: tuple | None = None) -> int:
    if g.op == 'const':
        return g.bit
    if g.op == 'not':
        return 1 - z[0]
    if g.op == 'xor':
        return sum(z) % 2
    if A is None:
        return int(all(z)) if g.op == 'and' else int(any(z))
    y = tuple(1 - q for q in z) if g.op == 'and' else z
    hashed = any(sum(a * q for a, q in zip(row, y)) % 2 for row in A)
    return 1 - int(hashed) if g.op == 'and' else int(hashed)

def bitargs(g: Gate, x: tuple, chronological: list[int]) -> tuple:
    return tuple(int(g.op == 'and') if w is None else
                 x[w[1]] if w[0] == 'x' else chronological[w[1]] for w in g.refs)

def table(gates: tuple[Gate, ...], x: tuple, A: tuple | None = None) -> list[int]:
    out: list[int] = []
    for g in gates:
        out.append(bitgate(g, bitargs(g, x, out), A))
    return out

def poly_gate(n: int, g: Gate, newest: list[Poly], A: tuple) -> Poly:
    O = one(n)
    z: list[Poly] = []  # no Boolean multilinear reduction
    for w in g.refs:
        z.append((O if g.op == 'and' else frozenset()) if w is None else
                 var(n, w[1]) if w[0] == 'x' else newest[len(newest)-1-w[1]])
    if g.op == 'const':
        return O if g.bit else frozenset()
    if g.op == 'not':
        return O ^ z[0]
    if g.op == 'xor':
        out = frozenset()
        for q in z:
            out ^= q
        return out
    if g.op == 'and':
        z = [O ^ q for q in z]
    out = O
    for row in A:
        h = frozenset()
        for a, q in zip(row, z):
            if a:
                h ^= q
        out = mul(out, O ^ h)
    return out if g.op == 'and' else O ^ out

def heights(gates: tuple[Gate, ...]) -> list[int]:
    ds: list[int] = []
    for g in gates:
        h = max((ds[w[1]] if w is not None and w[0] == 'g' else 0 for w in g.refs), default=0)
        ds.append(h + int(g.op in ('and', 'or')))
    return ds

def check(n: int, K: int, gates: tuple[Gate, ...], top: Gate, r: int, t: int,
          counts: Counter, coupled: bool = False) -> None:
    require(top.op in ('and', 'or') and len(top.refs) == K, 'root restriction')
    require(r >= 1 and t >= 0, 'row range')
    S = sum(g.op in ('and', 'or') for g in gates)
    ds = heights(gates)
    H = max((ds[w[1]] if w is not None and w[0] == 'g' else 0 for w in top.refs), default=0)
    xs = tuple(product((0, 1), repeat=n))
    true = [table(gates, x) for x in xs]
    failures = [0] * len(xs)
    counts['parameter_cases'] += 1
    As, Bs = matrices(K, r), matrices(K, t)
    require(not coupled or t <= r, 'prefix coupling needs t<=r')
    for A in As:
        newest: list[Poly] = []
        for g in gates:
            newest.insert(0, poly_gate(n, g, newest, A))
        approx = [table(gates, x, A) for x in xs]
        bad = [any(bitgate(g, bitargs(g, x, truth[:j]), A) != truth[j]
                   for j, g in enumerate(gates)) for x, truth in zip(xs, true)]
        for B in (A[:t],) if coupled else Bs:
            q = poly_gate(n, top, newest, B)
            require(degree(q) <= t*r**H, 'actual degree bound')
            counts['polynomial_samples'] += 1
            for i, x in enumerate(xs):
                val = bitgate(top, bitargs(top, x, approx[i]), B)
                expected = bitgate(top, bitargs(top, x, true[i]))
                rootbad = bitgate(top, bitargs(top, x, true[i]), B) != expected
                require(peval(q, x) == val, 'polynomial/Boolean evaluation')
                require(val == expected or bad[i] or rootbad, 'true-child error inclusion')
                failures[i] += val != expected
                counts['pointwise_evaluations'] += 1
    space = len(As) if coupled else len(As)*len(Bs)
    for f in failures:
        require(Fraction(f, space) <= Fraction(S, 2**r)+Fraction(1, 2**t), 'error budget')
        counts['pointwise_bounds'] += 1
        if t == 2 and 12*S <= 2**r:
            require(3*f <= space, 'one-third endpoint')
            counts['one_third_bounds'] += 1

def gates(n: int, K: int):
    yield Gate('const', bit=0)
    yield Gate('const', bit=1)
    for j in range(n):
        yield Gate('not', (('x', j),))
    refs = (None,) + tuple(('x', j) for j in range(n))
    for ws in product(refs, repeat=K):
        for op in ('or', 'and', 'xor'):
            yield Gate(op, ws)

def cascade_error(r: int, t: int) -> Fraction:
    fail = 0
    for A in matrices(1, r):
        v = bitgate(Gate('or'), (1,), A)
        for B in matrices(1, t):
            fail += bitgate(Gate('or'), (v,), B) != 1
    return Fraction(fail, len(matrices(1, r))*len(matrices(1, t)))

def main() -> None:
    counts, deeper, coupled = Counter(), Counter(), Counter()
    structures = 0
    for n in range(3):
        for K in range(3):
            for inner in ((),) + tuple((g,) for g in gates(n, K)):
                refs = (None,) + tuple(('x', j) for j in range(n)) + tuple(('g', j) for j in range(len(inner)))
                for ws in product(refs, repeat=K):
                    for op in ('or', 'and'):
                        structures += 1
                        for r in (1, 2):
                            for t in (0, 1, 2):
                                check(n, K, inner, Gate(op, ws), r, t, counts)
    x0, x1, g0, g1, g2 = ('x', 0), ('x', 1), ('g', 0), ('g', 1), ('g', 2)
    cases = (
        (2, 2, (Gate('or', (x0, x1)), Gate('xor', (g0, x0))), Gate('and', (g0, g1))),
        (2, 2, (Gate('and', (x0, None)), Gate('not', (g0,))), Gate('or', (g0, g1))),
        (2, 2, (Gate('or', (x0, x1)), Gate('and', (g0, g0))), Gate('or', (g1, g0))),
        (2, 2, (Gate('or', (x0, x1)), Gate('and', (g0, g0)), Gate('or', (g1, None))), Gate('and', (x0, None))),
        (0, 0, (Gate('and', ()), Gate('or', ())), Gate('and', ())),
        (2, 2, (Gate('const', bit=1), Gate('xor', (g0, x0)), Gate('and', (g1, x1))), Gate('or', (g2, g1))),
    )
    for c in cases:
        for r, t in ((1, 0), (1, 3), (2, 2), (5, 2)):
            check(*c, r, t, deeper)
        for r, t in ((2, 2), (5, 2)):
            check(*c, r, t, coupled, coupled=True)
    old = cascade_error(2, 2)
    repaired = cascade_error(4, 2)
    require(3 <= 2**2 and old == Fraction(7, 16) and old > Fraction(1, 3), 'old budget negative control')
    require(repaired == Fraction(19, 64) and repaired <= Fraction(1, 3), 'new budget control')
    q = poly_gate(1, Gate('or', (('x', 0),)), [], ((1,), (1,)))
    qq = poly_gate(1, Gate('or', (('g', 0),)), [q], ((1,), (1,)))
    require(degree(q) == 2 and degree(qq) == 4 and peval(qq, (1,)) == 1, 'unreduced root factor')
    require(cascade_error(0, 2) == 1, 'zero inner rows negative control')
    print(json.dumps({'status': 'PASS', 'scope': 'finite exact controls; no generic or independent proof',
        'small_circuit_structures': structures, 'exhaustive': dict(counts),
        'deeper_structures': len(cases), 'deeper': dict(deeper),
        'prefix_coupling_only_finite': dict(coupled),
        'negative_controls': {'old_3S_budget_error': str(old), 'correct_12S_budget_error': str(repaired),
          'omitted_root_factor_actual_degree': degree(qq), 'claimed_without_factor': 2,
          'inner_r0_cascade_error': '1', 'arbitrary_XOR_extension': 'excluded; see graveyard/052'}},
        sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
