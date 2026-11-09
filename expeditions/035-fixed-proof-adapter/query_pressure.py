#!/usr/bin/env python3
"""Finite checks of a projection-rank counterfamily and query-weighted OR bound.
These corroborate the written identities, not novelty or a general formal proof.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def main():
    families = []
    for n in range(1,10):
        for k in range(1,n+1):
            # p(x)=1+prod_{j<k}(1+x_j) over GF2; target is constant one.
            value = lambda x: 1 ^ int(x & ((1 << k)-1) == 0)
            images = [z & ~((1 << k)-1) for z in range(1 << n)]
            errors = sum(value(x)==0 for x in range(1 << n))
            require(errors == 1 << (n-k), 'codimension error count')
            require(all(value(x)==0 for x in images), 'projection hits only errors')
            for y in set(images):
                require(images.count(y) == 1 << k, 'image fiber count')
            # Actual expansion: constant terms cancel, leaving all nonempty subsets of k.
            masks = tuple(range(1,1 << k))
            require(max(m.bit_count() for m in masks) == k, 'exact polynomial degree')
            require(all(sum(x&m==m for m in masks)%2 == value(x)
                        for x in range(1 << n)), 'GF2 expansion')
            families.append(dict(n=n,k=k,rank=n-k,uniform_error=str(F(errors,1<<n)),
                                 query_error='1',density=1 << k))
    # All proof/row/test instances on two addresses. Select a true literal once.
    checks = 0
    for pi in range(4):
        tests = [(a,s) for a in product(range(2),repeat=3)
                 for s in product(range(2),repeat=3)
                 if any(((pi>>x)&1)^v for x,v in zip(a,s))]
        weights = [F(i+1,len(tests)*(len(tests)+1)//2) for i in range(len(tests))]
        rho = [F(0),F(0)]
        for (a,s),w in zip(tests,weights):
            witness = next(j for j in range(3) if ((pi>>a[j])&1)^s[j])
            rho[a[witness]] += w
        require(sum(rho)==1,'pushforward normalization')
        density = 2*max(rho)
        for row in range(4):
            bad = [int(((row>>x)&1)!=((pi>>x)&1)) for x in range(2)]
            clause_failure = sum(w for (a,s),w in zip(tests,weights)
                                 if not any(((row>>x)&1)^v for x,v in zip(a,s)))
            weighted_error = sum(w*b for w,b in zip(rho,bad))
            require(clause_failure <= weighted_error <= density*F(sum(bad),2),
                    'query weighted error bound')
            checks += 1
    result = dict(status='PASS',scope='finite same-author corroboration; not a Lean theorem or independent review',
                  parameters='1<=n<=9, 1<=k<=n',examples=[families[0],families[-5],families[-1]],
                  family_cases=len(families),weighted_error_checks=checks,
                  self_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    print(json.dumps(result,sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
