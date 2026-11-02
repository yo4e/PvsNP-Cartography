#!/usr/bin/env python3
"""Finite continuation: parity lifting and exact block counts, not a runtime theorem.
Python >=3.10, standard library only. Checks remain enabled with -O.
"""
from collections import Counter
from math import comb
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def lift_coeffs(s):
    require(s >= 1, 'positive amplification parameter')
    h = 2*s-1
    a = [0]*(h+1)
    for j in range(s, h+1):
        for k in range(h-j+1):
            a[j+k] += comb(h,j)*comb(h-j,k)*(-1)**k
    return a


def multiply(p, q, mod):
    out = {}
    for a, c in p.items():
        for b, d in q.items():
            e = tuple(x+y for x,y in zip(a,b))
            out[e] = (out.get(e,0)+c*d) % mod
    return {e:c for e,c in out.items() if c}


def compose(n, terms, s):
    mod = 1 << s
    p = {tuple((mask >> j) & 1 for j in range(n)):1 for mask in terms}
    power, out = {(0,)*n:1}, {}
    for a in lift_coeffs(s):
        for e,c in power.items():
            out[e] = (out.get(e,0)+a*c) % mod
        power = multiply(power,p,mod)
    return {e:c for e,c in out.items() if c}


def pvalue(p, x):
    return sum(c for e,c in p.items() if all(not a or (x >> j)&1 for j,a in enumerate(e)))


def zeta(a):
    a = list(a)
    for bit in range((len(a)-1).bit_length()):
        for x in range(len(a)):
            if x >> bit & 1:
                a[x] += a[x ^ (1 << bit)]
    return a


def check(n, terms, ell, totals):
    require(0 <= ell <= n, 'block range')
    d = max((m.bit_count() for m in terms),default=0)
    head, mod = n-ell, 1 << (ell+1)
    actual = compose(n,terms,ell+1)
    require(max(map(sum,actual),default=0) <= (2*ell+1)*d, 'actual composition degree')
    reduced = {}
    for e,c in actual.items():
        mask = sum((a>0) << j for j,a in enumerate(e))
        reduced[mask] = (reduced.get(mask,0)+c) % mod
    reduced = {m:c for m,c in reduced.items() if c}
    require(max((m.bit_count() for m in reduced),default=0) <= (2*ell+1)*d, 'reduced degree')
    folded = [0]*(1 << head)
    for m,c in reduced.items():
        folded[m & ((1 << head)-1)] += c*(1 << (ell-(m >> head).bit_count()))
    fast = [v % mod for v in zeta(folded)]
    slow = [0]*(1 << head)
    for x in range(1 << n):
        parity = sum(x & m == m for m in terms) % 2
        require(pvalue(actual,x) % mod == parity, 'modulus lifting')
        require(sum(c for m,c in reduced.items() if x&m == m) % mod == parity,
                'squarefree evaluation')
        slow[x & ((1 << head)-1)] += parity
        totals['point_evaluations'] += 1
    require(all(0 <= v <= 1 << ell for v in slow), 'count range')
    require(fast == slow, 'no-wrap block count equals brute force')
    totals['polynomial_block_cases'] += 1
    totals['exact_block_counts'] += len(slow)


def main():
    tests = 0
    for s in range(1,7):
        a = lift_coeffs(s)
        for y in range(-32,33):
            direct = sum(comb(2*s-1,j)*y**j*(1-y)**(2*s-1-j) for j in range(s,2*s))
            require(sum(c*y**j for j,c in enumerate(a)) == direct, 'coefficient expansion')
            require(direct % (1 << s) == y % 2, 'all-integer parity lift control')
            tests += 1
    totals, structures = Counter(), 0
    for n,d in ((0,0),(1,1),(2,2),(3,2),(4,1)):
        supports = [m for m in range(1 << n) if m.bit_count() <= d]
        for mask in range(1 << len(supports)):
            terms = tuple(m for j,m in enumerate(supports) if mask >> j & 1)
            structures += 1
            for ell in range(n+1):
                check(n,terms,ell,totals)
    for terms in ((3,12,48),(0,1,2,4,8,16,32),(7,56),(0,),()):
        structures += 1
        for ell in range(7):
            check(6,terms,ell,totals)
    wrap = []
    for ell in range(7):
        count = 1 << ell
        require(count % (1 << ell) == 0 and count % (1 << (ell+1)) == count,
                'strictly larger modulus is essential')
        wrap.append(dict(ell=ell,count=count,wrong_residue=0))
    print(json.dumps(dict(status='PASS', scope='finite local continuation, not a Lean proof or speedup theorem',
                         integer_lift_tests=tests,polynomial_structures=structures,
                         counts=dict(totals),wrap_counterexamples=wrap),sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
