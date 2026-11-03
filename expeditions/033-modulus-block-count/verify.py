#!/usr/bin/env python3
"""Exact finite controls for the modulus bridge; not a general or independent proof.
Python >=3.10, standard library only. All checks remain active under python -O.
Exponent-vector composition, squarefree quotient-ring Horner composition, direct
integer evaluation and brute GF2 block counts are separate same-author paths.
"""
from __future__ import annotations
from collections import Counter
from functools import lru_cache
from itertools import product
from math import comb, prod
import json


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


@lru_cache(maxsize=None)
def coefficients(s: int) -> tuple[int, ...]:
    require(s >= 1, 'positive s')
    h = 2*s-1
    out = [0]*(h+1)
    for j in range(s, h+1):
        for k in range(h-j+1):
            out[j+k] += comb(h,j)*comb(h-j,k)*(-1)**k
    return tuple(out)


def bernstein(s: int, value: int) -> int:
    return sum(comb(2*s-1,j)*value**j*(1-value)**(2*s-1-j)
               for j in range(s,2*s))


def horner(s: int, value: int) -> int:
    acc = 0
    for c in reversed(coefficients(s)):
        acc = acc*value+c
    return acc


def clean(p: dict, modulus: int) -> dict:
    return {e: c % modulus for e,c in p.items() if c % modulus}


def sparse_mul(p: dict, q: dict, modulus: int, squarefree: bool) -> dict:
    out = {}
    for e,c in p.items():
        for f,d in q.items():
            key = e | f if squarefree else tuple(a+b for a,b in zip(e,f))
            out[key] = (out.get(key,0)+c*d) % modulus
    return clean(out,modulus)


def quotient_compose(p: dict[int,int], s: int) -> dict[int,int]:
    modulus = 1 << s
    acc = {}
    for c in reversed(coefficients(s)):
        acc = sparse_mul(acc,p,modulus,True)
        acc[0] = (acc.get(0,0)+c) % modulus
        acc = clean(acc,modulus)
    return acc


def unreduced_compose(n: int, p: dict[tuple,int], s: int) -> dict[tuple,int]:
    modulus, zero = 1 << s, (0,)*n
    power, out = {zero:1}, {}
    for j,c in enumerate(coefficients(s)):
        for e,v in power.items():
            out[e] = (out.get(e,0)+c*v) % modulus
        if j+1 < len(coefficients(s)):
            power = sparse_mul(power,p,modulus,False)
    return clean(out,modulus)


def reduce_polynomial(p: dict[tuple,int], modulus: int) -> dict[int,int]:
    out = {}
    for e,c in p.items():
        key = sum((a > 0) << j for j,a in enumerate(e))
        out[key] = (out.get(key,0)+c) % modulus
    return clean(out,modulus)


def actual_eval(p: dict[tuple,int], x: int) -> int:
    return sum(c*prod(((x >> j)&1)**a for j,a in enumerate(e)) for e,c in p.items())


def mask_eval(p: dict[int,int], x: int) -> int:
    return sum(c for mask,c in p.items() if mask & x == mask)


def submasks(mask: int):
    sub = mask
    while True:
        yield sub
        if not sub:
            return
        sub = (sub-1)&mask


def zeta_checked(original: list[int], modulus: int, stats: Counter) -> list[int]:
    """Check EACH stage, not just final outputs: processed-bit subset invariant."""
    n = (len(original)-1).bit_length()
    require(len(original) == 1 << n, 'zeta arity')
    out = [v % modulus for v in original]
    for k in range(n+1):
        processed = (1 << k)-1
        for x in range(1 << n):
            expected = sum(original[(x & ~processed)|u] for u in submasks(x & processed)) % modulus
            require(out[x] == expected, 'zeta stage invariant')
            stats['zeta_stage_entries'] += 1
        if k < n:
            for x in range(1 << n):
                if x >> k & 1:
                    out[x] = (out[x]+out[x ^ (1 << k)]) % modulus
    return out


def block_check(n: int, p: dict[tuple,int], ell: int, stats: Counter,
                check_unreduced: bool) -> None:
    require(0 <= ell <= n, 'block range')
    modulus, head = 1 << (ell+1), n-ell
    degree = max(map(sum,p),default=0)
    reduced_lift = reduce_polynomial(p,modulus)
    q = quotient_compose(reduced_lift,ell+1)
    require(max((m.bit_count() for m in q),default=0) <= (2*ell+1)*degree,
            'squarefree composition degree')
    if check_unreduced:
        raw = unreduced_compose(n,p,ell+1)
        require(max(map(sum,raw),default=0) <= (2*ell+1)*degree, 'actual composition degree')
        require(reduce_polynomial(raw,modulus) == q, 'unreduced and quotient Horner mismatch')
        stats['unreduced_compositions'] += 1
    folded = [0]*(1 << head)
    for mask,c in q.items():
        tail = mask >> head
        folded[mask & ((1 << head)-1)] += c*(1 << (ell-tail.bit_count()))
    fast = zeta_checked(folded,modulus,stats)
    expected = [0]*(1 << head)
    direct_amplified = [0]*(1 << head)
    for x in range(1 << n):
        lifted = actual_eval(p,x)
        bit = lifted % 2
        expected[x & ((1 << head)-1)] += bit
        direct_amplified[x & ((1 << head)-1)] += bernstein(ell+1,lifted)
        require(mask_eval(q,x) % modulus == bit, 'original GF2 versus quotient value')
        if check_unreduced:
            require(actual_eval(raw,x) % modulus == bit, 'original GF2 versus unreduced value')
        stats['pointwise_checks'] += 1
    require(fast == expected, 'folded exact count mismatch')
    require([v % modulus for v in direct_amplified] == expected, 'direct amplifier sum mismatch')
    require(all(0 <= v <= 1 << ell < modulus for v in expected), 'strict no-wrap interval')
    stats['polynomial_block_cases'] += 1
    stats['exact_block_counts'] += len(expected)


def integer_checks() -> dict:
    count = 0
    for s in range(1,13):
        require(len(coefficients(s)) == 2*s, 'amplifier degree')
        for y in range(-64,65):
            v = bernstein(s,y)
            require(v == horner(s,y), 'integer implementations mismatch')
            require(v % (1 << s) == y % 2, 'signed integer congruence')
            count += 1
    return dict(s_range=[1,12],integer_range=[-64,64],cases=count)


def main() -> None:
    exhaustive, powers, signed = Counter(), Counter(), Counter()
    structures = 0
    # All Boolean squarefree polynomials of the stated degree, not sampled rows.
    for n,d in ((0,0),(1,1),(2,2),(3,2),(4,2)):
        supports = [m for m in range(1 << n) if m.bit_count() <= d]
        for coeff in range(1 << len(supports)):
            p = {tuple((mask >> j)&1 for j in range(n)):1
                 for i,mask in enumerate(supports) if coeff >> i & 1}
            structures += 1
            for ell in range(n+1):
                block_check(n,p,ell,exhaustive,n<=2 or n==3 and ell<=2)
    # Non-squarefree source powers include Boolean cancellation x+x^2.
    actual_structures = 0
    for n,d in ((1,5),(2,3)):
        exponents = [e for e in product(range(d+1),repeat=n) if sum(e)<=d]
        for coeff in range(1 << len(exponents)):
            p = {e:1 for j,e in enumerate(exponents) if coeff >> j & 1}
            actual_structures += 1
            for ell in range(n+1):
                block_check(n,p,ell,powers,True)
    # Signed alternative integer lifts are tested as an extension, not as the
    # formal canonical-lift construction. Their mod-2 polynomials are the target.
    for coeffs in product((-3,-2,-1,0,1,2,3),repeat=3):
        p = {e:c for e,c in zip(((0,0),(1,0),(0,2)),coeffs) if c}
        for ell in range(3):
            block_check(2,p,ell,signed,True)
    require((1+1)%2 == 0 and 1+1 == 2, 'canonical lift not additive')
    require(2**2 != 2, 'Boolean-only reduction counterexample')
    require(bernstein(2,2) == -4 and 2%2 == 0, 'raw lift is not accepting count')
    require(sparse_mul({1:1},{1:1},4,True) == {1:1}, 'overlapping supports must survive')
    wrap = []
    for ell in range(9):
        k = 1 << ell
        require(k % k == 0 and k % (2*k) == k, 'known wrap control')
        wrap.append([ell,k])
    result = dict(status='PASS',scope='finite exact controls; same author; no general proof or speedup benchmark',
                  integers=integer_checks(),squarefree_structures=structures,exhaustive=dict(exhaustive),
                  actual_power_structures=actual_structures,powers=dict(powers),
                  signed_lift_structures=7**3,signed=dict(signed),
                  negative_controls=dict(lift_additivity=[0,2],off_cube_reduction=[4,2],
                    raw_amplifier_value=-4,correct_parity=0,overlap_product='x*x reduces to x, not zero',
                    previously_known_wrap=wrap))
    print(json.dumps(result,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
