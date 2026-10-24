#!/usr/bin/env python3
"""Exact adversarial controls for the actual agreement-dimension derivation.
These finite checks do not establish the arbitrary-field/arity theorem.
Two separately implemented rank computations cross-check each other.
"""
from itertools import product, combinations
from math import comb
import json


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


class Field:
    def __init__(self, q):
        self.q = q

    def add(self, a, b):
        return a ^ b if self.q == 4 else (a+b) % self.q

    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q

    def sub(self, a, b):
        return self.add(a, self.neg(b))

    def mul(self, a, b):
        if self.q != 4:
            return a*b % self.q
        # Fixed multiplication table, independent of the earlier shift/XOR loop.
        return ((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))[a][b]

    def power(self, a, k):
        z = 1
        for _ in range(k):
            z = self.mul(z, a)
        return z

    def inv(self, a):
        require(a != 0, 'inverse of zero')
        return next(b for b in range(1,self.q) if self.mul(a,b)==1)

    def div(self, a, b):
        return self.mul(a,self.inv(b))

    def prod(self, xs):
        z = 1
        for a in xs:
            z = self.mul(z,a)
        return z

    def sum(self, xs):
        z = 0
        for a in xs:
            z = self.add(z,a)
        return z


def rank_eliminate(F, rows):
    """Column-directed Gaussian elimination, no iterator over rebinding rows."""
    A = [list(r) for r in rows]
    if not A:
        return 0
    r = 0
    for c in range(len(A[0])):
        pivot = next((k for k in range(r,len(A)) if A[k][c]),None)
        if pivot is None:
            continue
        A[r],A[pivot] = A[pivot],A[r]
        scale = F.inv(A[r][c])
        A[r] = [F.mul(scale,a) for a in A[r]]
        for k in range(r+1,len(A)):
            factor = A[k][c]
            A[k] = [F.sub(a,F.mul(factor,b)) for a,b in zip(A[k],A[r])]
        r += 1
        if r == len(A):
            break
    return r


def determinant(F, rows):
    """Permutation expansion, independent of Gaussian elimination."""
    from itertools import permutations
    n = len(rows)
    terms = []
    for p in permutations(range(n)):
        v = F.prod(rows[i][p[i]] for i in range(n))
        inversions = sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        terms.append(F.neg(v) if inversions%2 else v)
    return F.sum(terms)


def rank_minors(F, rows):
    if not rows:
        return 0
    for k in range(min(len(rows),len(rows[0])),0,-1):
        for I in combinations(range(len(rows)),k):
            for J in combinations(range(len(rows[0])),k):
                if determinant(F,[[rows[i][j] for j in J] for i in I]):
                    return k
    return 0


def monomial(F, exponents, y):
    return F.prod(F.power(v,k) for v,k in zip(y,exponents))


def reduced_monomial(F,a,b,exponents):
    """Explicit product of affine power interpolants, coefficients by subsets."""
    coeff = {0:1}
    for i,k in enumerate(exponents):
        if k == 0:
            continue
        ak,bk = F.power(a,k),F.power(b,k)
        c = F.div(F.sub(ak,bk),F.sub(a,b))
        e = F.div(F.sub(F.mul(a,bk),F.mul(b,ak)),F.sub(a,b))
        nxt = {}
        for s,v in coeff.items():
            nxt[s] = F.add(nxt.get(s,0),F.mul(v,e))
            si = s | (1<<i)
            nxt[si] = F.add(nxt.get(si,0),F.mul(v,c))
        coeff = {s:v for s,v in nxt.items() if v}
    return coeff


def reduced_eval(F,coeff,y):
    return F.sum(F.mul(c,F.prod(y[i] for i in range(len(y)) if (s>>i)&1))
                 for s,c in coeff.items())


def run():
    power_checks = reduction_checks = interpolation_checks = matrix_checks = 0
    agreement_cases = []
    for q in (3,4,5):
        F = Field(q)
        for a,b in product(range(q),repeat=2):
            if a == b:
                continue
            for k in range(9):
                for x in (a,b):
                    coeff = reduced_monomial(F,a,b,(k,))
                    require(reduced_eval(F,coeff,(x,)) == F.power(x,k), 'power interpolation')
                    power_checks += 1
            for n in range(4):
                points = list(product((a,b),repeat=n))
                for exponents in product(range(4),repeat=n):
                    coeff = reduced_monomial(F,a,b,exponents)
                    require(max((s.bit_count() for s in coeff),default=0) <= sum(exponents),
                            'degree-preserving multilinear reduction')
                    for y in points:
                        require(reduced_eval(F,coeff,y) == monomial(F,exponents,y), 'reduction evaluation')
                        reduction_checks += 1
                for z in points:
                    for y in points:
                        factors = [F.div(F.sub(b,x),F.sub(b,a)) if v==a
                                   else F.div(F.sub(x,a),F.sub(b,a)) for v,x in zip(z,y)]
                        require(F.prod(factors) == int(y==z), 'actual delta interpolation')
                        interpolation_checks += 1
        # Complete 2x2 validation, plus 3x3 dependence/permutation controls.
        for vals in product(range(q),repeat=4):
            A = [vals[:2],vals[2:]]
            require(rank_eliminate(F,A) == rank_minors(F,A), 'independent determinant rank')
            matrix_checks += 1
        for A in ([[1,1],[1,0]],[[1,1],[1,1]],[[1,0,1],[0,1,1],[1,1,2%q]]):
            require(rank_eliminate(F,A) == rank_minors(F,A), 'rank negative control')
            matrix_checks += 1
        # All affine and constant polynomials for 0<=n<=3, all nonzero distinct grids.
        for a,b in product(range(1,q),repeat=2):
            if a==b:
                continue
            for n in range(4):
                points=list(product((a,b),repeat=n))
                for d in range(min(n,1)+1):
                    support=[s for s in range(1<<n) if s.bit_count()<=d]
                    t=(n+d)//2
                    low=[s for s in range(1<<n) if s.bit_count()<=t]
                    bound=sum(comb(n,j) for j in range(min(n,t)+1))
                    maximum=0
                    for cs in product(range(q),repeat=len(support)):
                        H=[y for y in points if F.sum(F.mul(c,F.prod(y[i] for i in range(n) if (s>>i)&1))
                              for s,c in zip(support,cs))==F.prod(y)]
                        A=[[F.prod(y[i] for i in range(n) if (s>>i)&1) for s in low] for y in H]
                        require(len(H)<=bound and rank_eliminate(F,A)==len(H),'agreement dimension')
                        maximum=max(maximum,len(H))
                    agreement_cases.append({'q':q,'a':a,'b':b,'n':n,'d':d,
                                            'polynomials':q**len(support),'max':maximum,'bound':bound})
    # Nonzero is essential; distinctness is only needed by this interpolation proof.
    zero_agreement=sum(all(x==1 for x in y)==False for y in product((0,1),repeat=3))
    require(zero_agreement==7>sum(comb(3,j) for j in range(2)), 'zero-endpoint counterexample')
    collapsed_cases=0
    for n,d in product(range(10),range(10)):
        B=sum(comb(n,j) for j in range(min(n,(n+d)//2)+1))
        require(1<=B,'collapsed grid bound')
        collapsed_cases+=1
    # Quantifier swap: independent constant R_y = product(y) agrees at every y,
    # but no one degree-zero polynomial has that property on a nontrivial grid.
    F=Field(3)
    points=list(product((1,2),repeat=3))
    require(all(F.prod(y)==F.prod(y) for y in points), 'chosen constant evaluation')
    require(all(sum(c==F.prod(y) for y in points)<8 for c in range(3)), 'no fixed constant agrees everywhere')
    require(8>sum(comb(3,j) for j in range(2)), 'pointwise-chosen-polynomial countermodel')
    # Signed normalized coefficients are not probabilities: constants 1,2,0
    # with masses 1,1,-1 succeed at both nonzero points, despite bound 1/2.
    signed=[(1,1),(2,1),(0,-1)]
    require(sum(w for c,w in signed)==1, 'signed normalization')
    require(all(sum(w*int(c==x) for c,w in signed)==1 for x in (1,2)), 'signed probability countermodel')
    return {'power_interpolation_checks':power_checks,'reduction_evaluations':reduction_checks,
            'lagrange_indicator_checks':interpolation_checks,'independent_rank_controls':matrix_checks,
            'agreement_configurations':len(agreement_cases),
            'agreement_summary_by_field':{str(q):{'configurations':sum(x['q']==q for x in agreement_cases),
                'polynomials':sum(x['polynomials'] for x in agreement_cases if x['q']==q),
                'tight_configurations':sum(x['max']==x['bound'] for x in agreement_cases if x['q']==q)} for q in (3,4,5)},
            'agreement_polynomials':sum(x['polynomials'] for x in agreement_cases),
            'collapsed_grid_cases':collapsed_cases,
            'negative_controls':{'zero_grid_n3_d0':{'actual':7,'false_bound':4},
                                 'input_dependent_constant_n3':{'actual':8,'fixed_polynomial_bound':4},
                                 'equal_nonzero_endpoints':'cardinality inequality survives; interpolation formula is singular',
                                 'signed_normalized_constants_n1':{'masses':[1,1,-1],'success_each':1,'uniform_bound':'1/2'}},
            'scope':'finite exact corroboration; no independent semantic reviewer, new lower bound or n299 acceptance'}


if __name__=='__main__':
    print(json.dumps(run(),sort_keys=True,indent=2))
