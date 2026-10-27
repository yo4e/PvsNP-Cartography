#!/usr/bin/env python3
"""Exact finite controls for Expedition026, not the generic Lean proof.
Sparse polynomial substitution is checked against separate Boolean evaluation.
GF4 table arithmetic is cross-checked with a quotient-polynomial implementation.
No external dependencies. Deterministic seed and explicit failure checks.
"""
from fractions import Fraction as F
from itertools import product
from math import comb
import json
import random

TABLE = ((0,0,0,0),(0,1,2,3),(0,2,3,1),(0,3,1,2))

def require(ok, message):
    if not ok:
        raise RuntimeError(message)

def mul(a,b):
    return TABLE[a][b]

def quotient_mul(a,b):
    z=0
    while b:
        if b&1: z ^= a
        b >>= 1
        a <<= 1
        if a&4: a ^= 7
    return z

def power(a,k):
    z=1
    for _ in range(k): z=mul(z,a)
    return z

def padd(p,q):
    r=p.copy()
    for e,c in q.items():
        r[e]=r.get(e,0)^c
        if not r[e]: del r[e]
    return r

def scale(p,c):
    return {e:mul(c,v) for e,v in p.items() if mul(c,v)}

def pmul(p,q):
    r={}
    for e,a in p.items():
        for f,b in q.items():
            g=tuple(x+y for x,y in zip(e,f))
            r[g]=r.get(g,0)^mul(a,b)
    return {e:c for e,c in r.items() if c}

def substitute(p,b,m):
    """Prepend two equal bits and substitute x_j=alpha*(y_j+1)."""
    result={}
    zero=(0,)*m
    for e,c in p.items():
        if b==0 and (e[0] or e[1]): continue
        term={zero:c}
        for j,k in enumerate(e[2:]):
            unit=tuple(int(i==j) for i in range(m))
            affine={zero:2,unit:2}
            for _ in range(k): term=pmul(term,affine)
        result=padd(result,term)
    return result

def transport(p,m):
    return padd(padd({(0,)*m:3},scale(substitute(p,0,m),2)),substitute(p,1,m))

def peval(p,y):
    z=0
    for e,c in p.items():
        term=c
        for a,k in zip(y,e): term=mul(term,power(a,k))
        z ^= term
    return z

def beval(p,x):
    """GF2 source evaluation, independent of field table and substitution."""
    z=0
    for e,c in p.items():
        require(c in (0,1),'source coefficient not GF2')
        z ^= c*int(all(k==0 or bit==1 for k,bit in zip(e,x)))
    return z

def target(x):
    return int(sum(x)%3==0)

def degree(p):
    return max((sum(e) for e,c in p.items() if c),default=0)

def from_truth(truth,n):
    cs=truth.copy()
    for j in range(n):
        for s in range(1<<n):
            if s>>j&1: cs[s] ^= cs[s^(1<<j)]
    return {tuple((s>>j)&1 for j in range(n)):1 for s,c in enumerate(cs) if c}

def main():
    field_checks=0
    for a,b in product(range(4),repeat=2):
        require(mul(a,b)==quotient_mul(a,b),'independent GF4 multiplication')
        field_checks+=1
    require(power(2,3)==1 and power(2,2)^2==1,'actual primitive root')
    for a,b,c in product(range(4),repeat=3):
        require(mul(a,b^c)==mul(a,b)^mul(a,c),'distributivity')
        require(mul(mul(a,b),c)==mul(a,mul(b,c)),'associativity')
        field_checks+=2
    polynomials=evaluations=0
    quadratic_counts=[]
    def check(p,m):
        nonlocal polynomials,evaluations
        q=transport(p,m)
        require(degree(q)<=degree(p),'actual total degree increased')
        for x in product((0,1),repeat=m):
            y=tuple(1 if bit==0 else 2 for bit in x)
            a0=beval(p,(0,0)+x)
            a1=beval(p,(1,1)+x)
            encoded=3^mul(2,a0)^a1
            require(peval(q,y)==encoded,'polynomial substitution vs source evaluation')
            root=power(2,sum(x))
            require(root==3^mul(2,target((0,0)+x))^target((1,1)+x),'residue target')
            c0=int(a0==target((0,0)+x)); c1=int(a1==target((1,1)+x))
            ct=int(encoded==root)
            require(ct==c0*c1,'encoding is injective on answer pairs')
            require(c0+c1-1<=ct,'same-index union bound')
            evaluations+=1
        polynomials+=1
    for m in range(3):
        n=m+2
        es=[tuple((s>>j)&1 for j in range(n)) for s in range(1<<n) if s.bit_count()<=2]
        before=polynomials
        for mask in range(1<<len(es)):
            check({e:1 for j,e in enumerate(es) if mask>>j&1},m)
        quadratic_counts.append({'m':m,'n':n,'polynomials':polynomials-before})
    high_start=polynomials
    for m in range(4):
        for e in product(range(4),repeat=m+2): check({e:1},m)
    rng=random.Random(2601027)
    for m in range(4):
        for _ in range(32):
            p={tuple(rng.randrange(5) for _ in range(m+2)):1 for _ in range(6)}
            check(p,m)
    high_count=polynomials-high_start

    # Genuine MOD3 polynomial family saturating the same-index union bound.
    n,m=3,1
    truth=[target(tuple((s>>j)&1 for j in range(n))) for s in range(1<<n)]
    families=[]
    for flip in (None,0,3):  # errors at (0,0,0) and (1,1,0)
        ts=truth.copy()
        if flip is not None: ts[flip]^=1
        p=from_truth(ts,n)
        require(all(beval(p,tuple((s>>j)&1 for j in range(n)))==ts[s] for s in range(8)),
                'independent Mobius witness evaluation')
        families.append(p)
    original_min=min(sum(F(int(beval(p,x)==target(x)),3) for p in families)
                     for x in product((0,1),repeat=3))
    root_success=sum(F(int(peval(transport(p,1),(1,))==1),3) for p in families)
    require(original_min==F(2,3) and root_success==F(1,3),'tight actual polynomial coupling')
    require(root_success < original_min**2,'false independence surrogate')

    # Nonuniform exact rational controls on the same actual family.
    weighted_checks=0
    for raw in product(range(4),repeat=3):
        if not sum(raw): continue
        mu=[F(a,sum(raw)) for a in raw]
        orig=min(sum(w*int(beval(p,x)==target(x)) for p,w in zip(families,mu))
                 for x in product((0,1),repeat=3))
        for x in product((0,1),repeat=1):
            y=tuple(1 if bit==0 else 2 for bit in x)
            got=sum(w*int(peval(transport(p,1),y)==power(2,sum(x))) for p,w in zip(families,mu))
            require(got>=2*orig-1,'nonuniform real-linear union bound control')
            weighted_checks+=1

    # Signed mass one can defeat the SAME transport even with apparent source
    # success in [0,1]. Error sets {110}, {000}, {000,110} with weights 2/3,2/3,-1/3.
    signed_family=[]
    for flips in ((3,),(0,),(0,3)):
        ts=truth.copy()
        for flip in flips: ts[flip]^=1
        signed_family.append(from_truth(ts,3))
    signed_weights=[F(2,3),F(2,3),F(-1,3)]
    signed_source_min=min(sum(w*int(beval(p,x)==target(x)) for p,w in zip(signed_family,signed_weights))
                          for x in product((0,1),repeat=3))
    signed_transport=sum(w*int(peval(transport(p,1),(1,))==1)
                         for p,w in zip(signed_family,signed_weights))
    require(sum(signed_weights)==1 and signed_source_min==F(2,3) and signed_transport==0,
            'nonnegative mass is essential to the union transport')

    # Explicit bad alternatives and preserved scope boundaries.
    require(3^mul(2,target((0,0,1)))^target((0,1,1)) != 2,'wrong padding must fail')
    require(3^target((0,0,0))^mul(2,target((1,1,0))) != 1,'swapped coefficient must fail')
    require(not any((2*a)%4==1 for a in range(4)),'ZMod4 is not GF4')
    independent15=sum(F(comb(15,k)*2**(15-k),3**15) for k in range(8,16))
    require(independent15==F(422009,4782969)<F(1,3),'independent versus reused majority draw')
    masks=lambda p:sorted(sum(ei<<j for j,ei in enumerate(e)) for e in p)
    return {'field_identity_checks':field_checks,'quadratic_exhaustive':quadratic_counts,
      'nonmultilinear_and_seeded_polynomials':high_count,'polynomials_total':polynomials,
      'transport_input_evaluations':evaluations,'nonuniform_mixture_checks':weighted_checks,
      'seed':2601027,
      'tight_coupling':{'source_n':3,'source_anf_masks':[masks(p) for p in families],
        'weights':['1/3']*3,'source_min_success':str(original_min),
        'transport_success_at_y1':str(root_success),'incorrect_independence_bound':'4/9'},
      'negative_controls':['one-bit-padding','swapped-root-coefficients','ZMod4-as-GF4','same-index-as-independent','signed-normalized-transport'],
      'signed_control':{'weights':['2/3','2/3','-1/3'],'source_min_success':str(signed_source_min),
                        'transport_success_at_y1':str(signed_transport),'false_lower_bound':'1/3'},
      'independent_majority15_error':str(independent15),'reused_majority15_error':'1/3',
      'scope':'finite exact checks only; generic theorem needs Lean; no novelty, independent semantic review or n299 acceptance'}

if __name__=='__main__':
    print(json.dumps(main(),sort_keys=True,indent=2))
