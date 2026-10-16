#!/usr/bin/env python3
"""Exact n=9 MOD3 certificate. Standard library only; checks work under -O.

The normalized witness samples ONE quadratic seed, then uniformly permutes
variables. A second implementation explicitly enumerates the 1260 distinct
partitions. Nothing here checks formal statements or establishes novelty.
"""
import json
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial
from pathlib import Path

N=9
PAIRS=list(combinations(range(N),2))

def require(ok,reason):
    if not ok: raise ValueError(reason)

def evaluate(row,x):
    c,a,b=row
    return (c+(a&x).bit_count()+
      sum((b>>k&1)*(x>>i&1)*(x>>j&1)
          for k,(i,j) in enumerate(PAIRS)))%2

def evaluate_second(row,x):
    c,a,b=row
    bits=[(x//(2**i))%2 for i in range(N)]
    return (c+sum((a//2**i%2)*bits[i] for i in range(N))+
      sum((b//2**k%2)*bits[i]*bits[j]
          for k,(i,j) in enumerate(PAIRS)))%2

def transform(table):
    ans=table[:]
    for i in range(N):
        for s in range(1<<N):
            if s>>i&1: ans[s]^=ans[s^(1<<i)]
    return ans

def walsh(a):
    a=a[:];size=1
    while size<len(a):
        for off in range(0,len(a),2*size):
            for i in range(off,off+size):
                u,v=a[i],a[i+size]
                a[i],a[i+size]=u+v,u-v
        size*=2
    return a

def verify(d):
    require(d['n']==9 and d['field']=='GF(2)' and d['error']=='1/3',
            'field, arity or error changed')
    require(d['target']=='weight divisible by 3','target changed')
    require(d['pair_order']=='lexicographic unordered pairs','wrong pair order')
    s=d['seed'];row=(s['constant'],s['linear_mask'],s['quadratic_mask'])
    c,a,b=row
    require(c in (0,1) and 0<=a<1<<9 and 0<=b<1<<36,'invalid polynomial')
    true=[int(x.bit_count()%3==0) for x in range(512)]
    vals=[evaluate(row,x) for x in range(512)]
    require(vals==[evaluate_second(row,x) for x in range(512)],
            'evaluators disagree')
    coefficients=transform(vals)
    expected=[0]*512;expected[0]=c
    for i in range(9):expected[1<<i]=a>>i&1
    for k,(i,j) in enumerate(PAIRS):
        expected[(1<<i)|(1<<j)]=b>>k&1
    require(coefficients==expected,'ANF reconstruction disagrees')
    require(all(x.bit_count()<=2 for x,p in enumerate(coefficients) if p),
            'degree exceeds two')
    sizes=[comb(9,w) for w in range(10)]
    good=[sum(vals[x]==true[x] for x in range(512) if x.bit_count()==w)
          for w in range(10)]
    require(good==d['layer_good'] and sizes==d['layer_sizes'],
            'layer counts differ')
    best=min(F(g,s) for g,s in zip(good,sizes))
    require(best==F(85,126) and best>F(2,3),'upper claim fails')

    # A full dual, NOT just sampled degree-one polynomials.
    mass=[d['dual_mass_by_weight'][x.bit_count()] for x in range(512)]
    D=d['dual_denominator']
    require(D==504 and min(mass)>=0 and sum(mass)==D,'bad dual mass')
    scores=[sum(mass[x] for x in range(512) if
         (c^((a&x).bit_count()&1))==true[x])
            for c in (0,1) for a in range(512)]
    w=walsh([mass[x]*(1-2*true[x]) for x in range(512)])
    independent=[(D+(1-2*c)*v)//2 for c in (0,1) for v in w]
    require(scores==independent,'direct and Walsh dual disagree')
    require(max(scores)==d['dual_affine_bound']==322 and
            F(max(scores),D)==F(23,36)<F(2,3),'degree-one obstruction fails')
    for k in range(10):
        odd=sum(comb(k,j)*comb(9-k,3-j)
                for j in (1,3) if j<=k and 0<=3-j<=9-k)
        formula=F(9-k,18)+F(odd,168)
        require(F(scores[(1<<k)-1],D)==formula and
                F(scores[512+(1<<k)-1],D)==1-formula,
                'hypergeometric affine check disagrees')
    return row,vals,true,{'upper_minimum':str(best),
            'layer_success':[str(F(g,s)) for g,s in zip(good,sizes)],
            'dual_maximum':str(F(max(scores),D)),
            'all_inputs':512,'affine_rows':1024}

def blocks(A,B,C,x):
    a=sum(x>>i&1 for i in A)
    b=sum(x>>i&1 for i in B)
    c=sum(x>>i&1 for i in C)
    return (1+a+b+comb(a,2)+a*b+b*c+comb(c,2))%2

def block_masks(A,B,C):
    a=sum(1<<i for i in A|B)
    b=sum(1<<k for k,(i,j) in enumerate(PAIRS)
          if (i in A and j in A) or (i in C and j in C) or
          (i in A and j in B) or (i in B and j in A) or
          (i in B and j in C) or (i in C and j in B))
    return 1,a,b

def partition_audit(d,row,true):
    A=set(d['block_partition']['A'])
    B=set(d['block_partition']['B'])
    C=set(d['block_partition']['C'])
    require(len(A)==4 and len(B)==3 and len(C)==2
            and A|B|C==set(range(9)) and not(A&B or A&C or B&C),
            'not a valid 4/3/2 partition')
    require(block_masks(A,B,C)==row,'block representation changed')
    scores=[0]*512
    distinct=set()
    for aa in combinations(range(9),4):
        A=set(aa)
        rest=[i for i in range(9) if i not in A]
        for bb in combinations(rest,3):
            B=set(bb);C=set(rest)-B
            r=block_masks(A,B,C)
            require(r not in distinct,'partitions collapse unexpectedly')
            distinct.add(r)
            for x in range(512):
                q=blocks(A,B,C,x)
                require(q==evaluate(r,x),'block/direct polynomial disagreement')
                scores[x]+=q==true[x]
    require(len(distinct)==1260,'incorrect partition support')
    by_weight=[sorted({scores[x] for x in range(512) if x.bit_count()==w})
               for w in range(10)]
    expected=[1260*d['layer_good'][w]//comb(9,w) for w in range(10)]
    require(by_weight==[[v] for v in expected] and min(scores)==850,
            'all-input uniform partition distribution is invalid')
    return {'distinct_polynomials':len(distinct),
            'evaluations':1260*512,
            'denominator':1260,
            'integer_success_by_weight':expected,
            'minimum':'850/1260'}

def permutation_audit(vals,true,good):
    tally=[0]*10
    for e in permutations(range(9)):
        mask=0
        for w in range(10):
            tally[w]+=vals[mask]==int(w%3==0)
            if w<9:mask|=1<<e[w]
    expected=[good[w]*factorial(w)*factorial(9-w) for w in range(10)]
    require(tally==expected,'full permutation action differs')
    return {'permutations':factorial(9),'orbit_input_pairs':10*factorial(9)}

def main():
    import argparse,copy
    parser=argparse.ArgumentParser()
    parser.add_argument('--full',action='store_true')
    args=parser.parse_args()
    d=json.loads(Path(__file__).with_name('certificate.json').read_text())
    row,vals,true,result=verify(d)
    bad=[]
    for name,key,value in [('constant','constant',0),
                           ('quadratic','quadratic_mask',0),
                           ('linear','linear_mask',0)]:
        broken=copy.deepcopy(d);broken['seed'][key]=value
        try:verify(broken)
        except ValueError:bad.append(name)
        else:raise ValueError('invalid seed passed: '+name)
    for name,key,value in [('target','target','wrong'),
                           ('dual','dual_denominator',503),
                           ('bound','dual_affine_bound',321),
                           ('threshold','error','1/2')]:
        broken=copy.deepcopy(d);broken[key]=value
        try:verify(broken)
        except ValueError:bad.append(name)
        else:raise ValueError('invalid claim passed: '+name)
    report={'scope':'exact finite n9, same-author checks, not standalone Lean',
            'result':result,'mutations_rejected':bad}
    if args.full:
        report['partition']=partition_audit(d,row,true)
        report['permutation']=permutation_audit(vals,true,d['layer_good'])
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__=='__main__': main()
