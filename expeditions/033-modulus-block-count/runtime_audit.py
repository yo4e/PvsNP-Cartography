#!/usr/bin/env python3
"""Counted implementation and falsification controls, not a Lean runtime theorem.
Run beside the unchanged Expedition033 verify.py. Standard library, Python>=3.10.
Production functions do not enumerate Boolean tail inputs or verify their own
stage invariant by exponential subset enumeration. Tests do so separately.
"""
from __future__ import annotations
from itertools import groupby, product
from math import comb
from random import Random
import hashlib
import json
from pathlib import Path
import verify


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def support_bound(n: int, degree: int) -> int:
    require(n >= 0 and degree >= 0, 'nonnegative parameters')
    return sum(comb(n, k) for k in range(min(n, degree)+1))


def sorted_mul(p: list[tuple[int,int]], q: list[tuple[int,int]],
               modulus: int) -> tuple[list[tuple[int,int]], int]:
    """Deterministic sort-and-aggregate: no constant-time hash assumption.
    Counts emitted pairs, including terms whose residue vanishes. Intermediate
    list memory is O(len(p)*len(q)), NOT O(number of distinct output supports).
    """
    pairs = sorted(((u | v, (c*d) % modulus) for u,c in p for v,d in q),
                   key=lambda z: z[0])
    out = []
    for mask, entries in groupby(pairs, key=lambda z: z[0]):
        value = 0
        for _, c in entries:
            value = (value+c) % modulus
        if value:
            out.append((mask,value))
    return out, len(pairs)


def table_zeta(c: list[int], modulus: int) -> tuple[list[int], int]:
    require(modulus > 0 and len(c) > 0 and len(c) & (len(c)-1) == 0,
            'positive modulus and power-of-two nonempty table')
    v, additions = [x % modulus for x in c], 0
    stride = 1
    while stride < len(v):
        for base in range(0, len(v), 2*stride):
            for offset in range(stride):
                lo = base+offset
                hi = lo+stride
                v[hi] = (v[hi]+v[lo]) % modulus
                additions += 1
        stride *= 2
    return v, additions


def canonical_source(n: int, masks: list[int]) -> list[tuple[int,int]]:
    """Worst-case deterministic validation, including the large-degree tail=0 case.
    Hash collisions must not turn duplicate detection into quadratic work.
    """
    require(n >= 0, 'nonnegative arity')
    require(all(0 <= m < 1 << n for m in masks), 'source support range')
    ordered = sorted(masks)
    require(all(u != v for u, v in zip(ordered, ordered[1:])),
            'source ANF must be canonical')
    return [(m,1) for m in ordered]


def block_counts(n: int, tail: int, masks: list[int]) -> tuple[list[int], dict]:
    """Input is canonical squarefree GF2 ANF: distinct n-bit masks, coefficient1.
    A general exponent-list input must first be normalized; its read cost is not
    hidden in the complexity statement. Zero and one are valid at n=0.
    """
    require(0 <= tail <= n, 'tail interval')
    source = canonical_source(n,masks)
    s, head = tail+1, n-tail
    modulus = 1 << s
    degree = max((m.bit_count() for m in masks), default=0)
    h = 2*s-1
    coeff = verify.coefficients(s)
    acc = [(0,coeff[h] % modulus)] if coeff[h] % modulus else []
    pairs, peak_pairs, peak_support = 0, 0, len(acc)
    for stage, c in enumerate(reversed(coeff[:-1]), start=1):
        acc, count = sorted_mul(acc, source, modulus)
        pairs += count
        peak_pairs = max(peak_pairs, count)
        value = c % modulus
        if acc and acc[0][0] == 0:
            value = (value+acc[0][1]) % modulus
            acc = acc[1:]
        if value:
            acc.insert(0, (0,value))
        # These checks only inspect stored support, not Boolean assignments.
        require(len(acc) <= support_bound(n, stage*degree), 'stage support bound')
        require(all(m.bit_count() <= stage*degree and 0 < v < modulus
                    for m,v in acc), 'stage degree/residue')
        peak_support = max(peak_support,len(acc))
    max_support = support_bound(n,h*degree)
    require(pairs <= h*len(masks)*max_support, 'Horner pair bound')
    folded = [0]*(1 << head)
    head_mask = (1 << head)-1
    for mask, c in acc:
        factor_power = tail-(mask >> head).bit_count()
        require(factor_power >= 0, 'tail support guard')
        idx = mask & head_mask
        folded[idx] = (folded[idx]+(c << factor_power)) % modulus
    out, additions = table_zeta(folded,modulus)
    expected_additions = 0 if head == 0 else head*(1 << (head-1))
    require(additions == expected_additions, 'table butterfly count')
    return out, dict(n=n,tail=tail,source_terms=len(masks),degree=degree,
        degree_budget=h*degree,support_budget=max_support,
        pair_bound=h*len(masks)*max_support,pairs=pairs,peak_pairs=peak_pairs,
        peak_support=peak_support,fold_terms=len(acc),table_cells=1 << head,
        zeta_additions=additions,residue_bits=s)


def naive_all(c: list[int]) -> tuple[list[int], int]:
    """Literal recursive-evaluation MODEL of scan, not execution of Lean code."""
    a = (len(c)-1).bit_length()
    leaves = 0
    def rec(i: int, mask: int) -> int:
        nonlocal leaves
        if i == a:
            leaves += 1
            return c[mask]
        value = rec(i+1,mask)
        if mask >> i & 1:
            value += rec(i+1,mask ^ (1 << i))
        return value
    return [rec(0,mask) for mask in range(1 << a)], leaves


def direct_counts(n: int, tail: int, masks: list[int]) -> list[int]:
    head = n-tail
    out = [0]*(1 << head)
    for x in range(1 << n):
        parity = 0
        for m in masks:
            if x & m == m:
                parity ^= 1
        out[x & ((1 << head)-1)] += parity
    return out


def main() -> None:
    expected_blob = '86fd6619fb243bb898689934c42aa7782df554bc'
    data = Path(verify.__file__).read_bytes()
    blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    require(blob == expected_blob, 'unchanged prerequisite verifier')
    cost_rows = []
    for a in range(13):
        c = [((j*7)%11)-5 for j in range(1 << a)]
        naive, leaves = naive_all(c)
        fast, adds = table_zeta(c,1 << 20)
        require(fast == [v % (1 << 20) for v in naive], 'recursive/table values')
        require(leaves == 3**a, 'recursive leaf calls')
        cost_rows.append(dict(head=a,naive_leaves=leaves,table_additions=adds))
    table_cases = 0
    for a in range(4):
        for values in product((-1,0,2), repeat=1 << a):
            for s in range(1,5):
                got,_ = table_zeta(list(values),1 << s)
                expected = [sum(values[u] for u in range(1 << a) if u & x == u) % (1 << s)
                            for x in range(1 << a)]
                require(got == expected,'exhaustive signed table')
                table_cases += 1
    cases, exact_counts, source_count = 0, 0, 0
    interesting = []
    sources = []
    for n in range(4):
        for bits in range(1 << (1 << n)):
            sources.append((n,[m for m in range(1 << n) if bits >> m & 1]))
    rng = Random(20261105)
    for n in range(4,9):
        for _ in range(16):
            sources.append((n,[m for m in range(1 << n)
                               if m.bit_count() <= 2 and rng.randrange(4) == 0]))
        sources.extend(((n,[]),(n,[0]),(n,[1 << i for i in range(n)])))
    for n,masks in sources:
        source_count += 1
        for tail in range(n+1):
            got,counts = block_counts(n,tail,masks)
            require(got == direct_counts(n,tail,masks),'source block counts')
            # Distinct same-author coefficient implementation, plus brute source.
            q = verify.quotient_compose({m:1 for m in masks},tail+1)
            f = [0]*(1 << (n-tail))
            for m,v in q.items():
                f[m & (len(f)-1)] += v*(1 << (tail-(m >> (n-tail)).bit_count()))
            check,_ = table_zeta(f,1 << (tail+1))
            require(got == check,'existing quotient path')
            cases += 1
            exact_counts += len(got)
            if masks == [1 << i for i in range(n)] and n in (4,8):
                interesting.append(counts)
    # One coordinate twice destroys the once-per-coordinate invariant.
    once,_ = table_zeta([1,0],4)
    twice,_ = table_zeta(once,4)
    require(once == [1,1] and twice == [1,2], 'duplicate coordinate attack')
    # Real source p=x+y, b=1, canonical amplifier modulo4: x+y+2xy.
    require(verify.quotient_compose({1:1,2:1},2) == {1:1,2:1,3:2}, 'XOR witness')
    good,_ = block_counts(2,1,[1,2])
    bad_fold = [0,0]
    for m,v in ((1,1),(2,1),(3,2)):
        bad_fold[m & 1] = (v*(1 << (1-(m >> 1).bit_count()))) % 4
    bad,_ = table_zeta(bad_fold,4)
    require(good == [1,1] and bad == [1,3], 'overwrite attack')
    # Exact finite corroboration of the written generating-function budget.
    budgets = 0
    for n in range(100,401):
        for d in range(1,n//100+1):
            b = n//(100*d)
            D = (2*b+1)*d
            mprod = support_bound(n,D)*support_bound(n,d)
            require(mprod**50 <= 1 << (31*n), '31/50 exponent budget')
            require(200*d*b >= n and 100*b <= n, 'floor and head bounds')
            budgets += 1
    require(9**4 < 2*8**4, 'exact rational exponent constant')
    print(json.dumps(dict(status='PASS',scope='finite checks and counted Python model; same author; not Lean runtime verification',
        prerequisite_blob=blob,recursion=cost_rows,exhaustive_table_cases=table_cases,
        polynomial_sources=source_count,polynomial_block_cases=cases,exact_block_counts=exact_counts,
        finite_budget_checks=budgets,instrumented_examples=interesting,
        attacks=dict(duplicate_coordinate=[once,twice],overwrite_fold=[good,bad]),
        self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()),indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
