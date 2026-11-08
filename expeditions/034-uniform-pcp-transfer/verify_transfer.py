#!/usr/bin/env python3
"""Finite, exact, same-author attacks for the conditional PCP/counting bridge.
Not a PCP construction, time-hierarchy proof, or independent semantic review.
Python >=3.10, standard library only. Checks remain active under -O.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations, combinations_with_replacement, product
from math import comb
from pathlib import Path
from random import Random
import hashlib
import importlib.util
import json
import sys

OLD = Path(__file__).resolve().parents[1] / '033-modulus-block-count'
sys.path.insert(0, str(OLD))
import runtime_audit as counter


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def xor_sum(terms) -> tuple[int, ...]:
    ordered = sorted(terms)
    out = []
    i = 0
    while i < len(ordered):
        j = i+1
        while j < len(ordered) and ordered[j] == ordered[i]:
            j += 1
        if (j-i) % 2:
            out.append(ordered[i])
        i = j
    return tuple(out)


def mul(p: tuple[int,...], q: tuple[int,...]) -> tuple[int,...]:
    return xor_sum(a | b for a in p for b in q)


def value(p: tuple[int,...], x: int) -> int:
    return sum(x & m == m for m in p) % 2


def degree(p: tuple[int,...]) -> int:
    return max((m.bit_count() for m in p), default=0)


def coordinate(code: int) -> tuple[int,...]:
    # 0,1 are constants; 2+2j is z_j; 3+2j is 1+z_j.
    if code < 2:
        return (0,) if code else ()
    return ((0,1 << ((code-2)//2)) if code % 2 else (1 << ((code-2)//2),))


def query(codes: tuple[int,...], z: int) -> int:
    bits = [code if code < 2 else ((z >> ((code-2)//2)) & 1) ^ (code % 2)
            for code in codes]
    return sum(bit << j for j,bit in enumerate(bits))


def substitute(p: tuple[int,...], codes: tuple[int,...]) -> tuple[int,...]:
    terms = []
    for monomial in p:
        acc = (0,)
        for j,code in enumerate(codes):
            if monomial >> j & 1:
                acc = mul(acc,coordinate(code))
        terms.extend(acc)
    return xor_sum(terms)


def clause_poly(p: tuple[int,...], queries, signs) -> tuple[int,...]:
    reject = (0,)
    for codes,sign in zip(queries,signs):
        literal = xor_sum((*substitute(p,codes), *((0,) if sign else ())))
        reject = mul(reject,xor_sum((0,*literal)))
    return xor_sum((0,*reject))


def clause_accept(table: int, addresses, signs) -> int:
    return int(any(((table >> a) & 1) ^ sign for a,sign in zip(addresses,signs)))


def projection_tests() -> dict:
    cases = points = 0
    for k,r in ((0,0),(1,1),(2,2),(3,2)):
        for coeff in range(1 << (1 << k)):
            p = tuple(m for m in range(1 << k) if coeff >> m & 1)
            for codes in product(range(2+2*r),repeat=k):
                got = substitute(p,codes)
                require(degree(got) <= degree(p),'projection degree increased')
                for z in range(1 << r):
                    require(value(got,z) == value(p,query(codes,z)),'projection value')
                    points += 1
                cases += 1
    rng = Random(20261108)
    clauses = blocks = counts = 0
    for k in range(4):
        for r in range(5):
            for _ in range(5):
                p = tuple(m for m in range(1 << k) if rng.randrange(2))
                queries = [tuple(rng.randrange(2+2*r) for _ in range(k)) for _ in range(3)]
                for signs in product(range(2),repeat=3):
                    q = clause_poly(p,queries,signs)
                    require(degree(q) <= 3*degree(p),'clause degree bound')
                    truth = [int(any(value(p,query(c,z)) ^ sign
                                     for c,sign in zip(queries,signs))) for z in range(1 << r)]
                    require([value(q,z) for z in range(1 << r)] == truth,'clause truth')
                    for tail in range(r+1):
                        got,_ = counter.block_counts(r,tail,list(q))
                        expected = [0]*(1 << (r-tail))
                        for z,v in enumerate(truth):
                            expected[z & (len(expected)-1)] += v
                        require(got == expected,'composed clause exact count')
                        blocks += 1
                        counts += len(got)
                    clauses += 1
    return dict(substitutions=cases,pointwise_comparisons=points,
                signed_clause_cases=clauses,clause_block_cases=blocks,exact_head_counts=counts)


def transfer_tests() -> dict:
    local = mixes = averaging = 0
    clauses = list(product(product(range(2),repeat=3),product(range(2),repeat=3)))
    for target in range(4):
        for rows in combinations_with_replacement(range(4),3):
            errors = [sum(((row >> a)&1) != ((target >> a)&1) for row in rows) for a in range(2)]
            if max(errors) > 1:
                continue
            mixes += 1
            accepted = []
            for addresses,signs in clauses:
                if not clause_accept(target,addresses,signs):
                    continue
                outcomes = [clause_accept(row,addresses,signs) for row in rows]
                witnesses = [j for j in range(3) if ((target >> addresses[j]) & 1) ^ signs[j]]
                witness = witnesses[0]
                require(3-sum(outcomes) <= errors[addresses[witness]],'sharp one-literal bound')
                accepted.append(outcomes)
                local += 1
            # Nonuniform test weights: one fixed good row still suffices in expectation.
            totals = [sum((j+1)*v[i] for j,v in enumerate(accepted)) for i in range(3)]
            mass = len(accepted)*(len(accepted)+1)//2
            require(max(totals)*3 >= 2*mass,'global averaging witness')
            averaging += 1
    fixed = [Fraction(clause_accept(t,(0,0,0),(0,0,0)) +
                      clause_accept(t,(0,0,0),(1,1,1)),2) for t in range(2)]
    independent = Fraction(sum(any(bits) for bits in product(range(2),repeat=3)),8)
    require(fixed == [Fraction(1,2)]*2 and independent == Fraction(7,8),'proof resampling attack')
    # A polynomial correct on 3/4 of the address cube fails at the sole queried address.
    p = (1,2,3)  # 1 + delta_00 = x+y+xy.
    require(sum(value(p,x) == 1 for x in range(4)) == 3,'average agreement')
    require(value(p,0) == 0,'query concentration attack')
    return dict(valid_three_row_mixtures=mixes,sharp_or_checks=local,weighted_averaging_checks=averaging,
                global_proof_acceptance=[str(v) for v in fixed],
                resample_per_occurrence_acceptance=str(independent),
                adapt_per_test_acceptance='1',average_only_agreement='3/4',concentrated_query_acceptance='0')


def prefix_search(n: int, clauses) -> tuple[int|None,int]:
    def sat(prefix):
        return any(all(((x >> j)&1) == bit for j,bit in enumerate(prefix)) and
                   all(clause_accept(x,a,s) for a,s in clauses) for x in range(1 << n))
    calls = 1
    if not sat([]):
        return None,calls
    prefix = []
    for _ in range(n):
        calls += 1
        prefix.append(0 if sat(prefix+[0]) else 1)
    return sum(v << j for j,v in enumerate(prefix)),calls


def prefix_tests() -> dict:
    cases = max_calls = 0
    for n in (1,2):
        literals = list(product(range(n),range(2)))
        pool = []
        for triple in combinations_with_replacement(literals,3):
            pool.append((tuple(t[0] for t in triple),tuple(t[1] for t in triple)))
        for size in range(4):
            for formula in combinations(pool,size):
                got,calls = prefix_search(n,formula)
                expected = next((sum(b << j for j,b in enumerate(bits))
                    for bits in product(range(2),repeat=n)
                    if all(clause_accept(sum(b << j for j,b in enumerate(bits)),a,s)
                           for a,s in formula)),None)
                require(got == expected,'lexicographic proof prefix search')
                require(calls <= n+1,'oracle call budget')
                cases += 1
                max_calls = max(max_calls,calls)
    return dict(explicit_formula_cases=cases,max_oracle_calls=max_calls,
                scope='brute finite model of explicit SAT-prefix queries, not an efficient SAT solver')


class CountedInt(int):
    equality = ordering = 0
    __hash__ = int.__hash__
    def __eq__(self,other):
        type(self).equality += 1
        return int.__eq__(self,other)
    def __ne__(self,other):
        type(self).equality += 1
        return int.__ne__(self,other)
    def __lt__(self,other):
        type(self).ordering += 1
        return int.__lt__(self,other)


def hash_tests() -> dict:
    rows = []
    P = sys.hash_info.modulus
    for t in (32,64,128,256,512,1024):
        plain = [j*P for j in range(t)]
        require(all(hash(m) == 0 for m in plain),'ordinary integer hash collisions')
        rng = Random(20261108+t)
        rng.shuffle(plain)
        wrapped = [CountedInt(m) for m in plain]
        CountedInt.equality = CountedInt.ordering = 0
        require(len(set(wrapped)) == t,'old validation semantics')
        old_eq = CountedInt.equality
        CountedInt.equality = CountedInt.ordering = 0
        n = max(plain).bit_length()
        got = counter.canonical_source(n,wrapped)
        new_eq,new_lt = CountedInt.equality,CountedInt.ordering
        require([(int(m),v) for m,v in got] == [(m,1) for m in sorted(plain)],'new validation semantics')
        require(new_eq == t-1,'adjacent duplicate comparisons')
        rows.append(dict(terms=t,arity=n,old_hash_equalities=old_eq,
                         sorted_comparisons=new_lt,adjacent_equalities=new_eq))
    invalid = 0
    for n,masks in ((1,[0,0]),(2,[1,2,1]),(0,[1]),(2,[-1]),(-1,[])):
        try:
            counter.canonical_source(n,masks)
        except RuntimeError:
            invalid += 1
        else:
            raise RuntimeError('invalid source accepted')
    return dict(modulus=P,cases=rows,invalid_inputs_rejected=invalid,
                scope='validation only; equality counts instrument an int subclass with ordinary int hash; no enormous dense table allocated')


def arithmetic_tests() -> dict:
    # Exact symbolic ledger; the constants below are a toy budget, not PCP constants.
    overhead = 12
    bad_lambda,good_lambda = Fraction(1,6000),Fraction(1,12000)
    bad_exponent = overhead-Fraction(1,600)/bad_lambda
    good_exponent = overhead-Fraction(1,600)/good_lambda
    require(bad_exponent == 2 and good_exponent == -8,'saving versus overhead')
    # Elementary amplification certificate: (8/9)^6 < 1/2.
    require(2*8**6 < 9**6,'amplification rational bound')
    tails = 0
    for c in range(1,7):
        for n in range(2,65):
            logceil = (n-1).bit_length()
            t = 12*c*logceil+1
            failure_numerator = sum(comb(t,j)*2**(t-j) for j in range((t+1)//2,t+1))
            require(failure_numerator*n**c <= 3**t,'exact majority error')
            tails += 1
    return dict(majority_cases=tails,toy_overhead=overhead,
                bad_lambda=str(bad_lambda),bad_power_of_n=str(bad_exponent),
                good_lambda=str(good_lambda),good_power_of_n=str(good_exponent),
                guessed_bits_n8_d2=sum(comb(8,j) for j in range(3)),
                deterministic_candidate_count_n8_d2=1 << sum(comb(8,j) for j in range(3)))


def main():
    source_files = [Path(__file__),OLD/'runtime_audit.py',OLD/'verify.py']
    result = dict(status='PASS',scope='finite exact same-author controls; no universal proof or novelty claim',
                  projections=projection_tests(),transfer=transfer_tests(),prefix=prefix_tests(),
                  hash_validation=hash_tests(),arithmetic=arithmetic_tests(),
                  sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in source_files})
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == '__main__':
    main()
