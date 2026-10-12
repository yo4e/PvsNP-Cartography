from itertools import combinations,permutations
from fractions import Fraction as F
from scipy.optimize import linprog, milp, LinearConstraint, Bounds
from math import comb
import numpy as np
n=7; pairs=list(combinations(range(n),2)); ix={p:i for i,p in enumerate(pairs)}
def permute(row,p):
 c,a,b=row
 return c,sum(1<<p[i] for i in range(n) if a>>i&1),sum(1<<ix[tuple(sorted((p[i],p[j])))] for k,(i,j) in enumerate(pairs) if b>>k&1)
def correctness(row):
 c,a,b=row
 masks=[(1<<i)|(1<<j) for k,(i,j) in enumerate(pairs) if b>>k&1]
 return np.array([int((c ^ ((a&x).bit_count()%2) ^ (sum(x&m==m for m in masks)%2))==int(x.bit_count()%3==0)) for x in range(1<<n)],dtype=int)
seed=(1,71,1887847)
cyclic=[tuple((i+k)%n for i in range(n)) for k in range(n)]
allrows=sorted({permute(seed,p) for p in permutations(range(n))})
orbmap={}
for row in allrows:
 orbit=tuple(sorted({permute(row,p) for p in cyclic}))
 orbmap[orbit[0]]=orbit
orbits=list(orbmap.values()); sym=[(0,0,0),(0,0,2097151),(0,127,0),(1,127,2097151)]
C=np.array([sum((correctness(r) for r in orbit),np.zeros(128,dtype=int)) for orbit in orbits]).T
S=np.array([correctness(r) for r in sym]).T
base=S@np.array([1,2,1,1])
mins=(C+base[:,None]).min(axis=0)
print('orbits',len(orbits),'best 12-uniform min',max(mins),'candidates',int(sum(mins>=8)))
if max(mins)>=8: print(orbits[int(np.argmax(mins))])
A=np.column_stack((S,C/7))
res=linprog(np.r_[np.zeros(A.shape[1]),-1.],A_ub=np.column_stack((-A,np.ones(128))),b_ub=np.zeros(128),A_eq=np.array([np.r_[np.ones(A.shape[1]),0]]),b_eq=[1],bounds=[(0,None)]*A.shape[1]+[(0,1)],method='highs')
print('max t',res.x[-1], 'support',[ (i,str(F(float(w)).limit_denominator(100000))) for i,w in enumerate(res.x[:-1]) if w>1e-8])
# Search small uniform multisets of polynomials closed under cyclic shifts.
B=np.column_stack((S,C)); mass=np.r_[np.ones(4),np.full(len(orbits),7)]
for D in [12,15,18,21,24,27,30,36,42,48,60,84]:
 r=milp(c=np.r_[np.ones(4)*.001,np.ones(len(orbits))],integrality=np.ones(B.shape[1]),bounds=Bounds(np.zeros(B.shape[1]),np.full(B.shape[1],np.inf)),constraints=[LinearConstraint(B,np.full(128,(2*D+2)//3),np.full(128,np.inf)),LinearConstraint(mass[None,:],[D],[D])],options={'time_limit':2})
 print('D',D,'success',r.success, 'message',r.message)
 if r.x is not None:
  weights=np.rint(r.x).astype(int)
  if (B@weights).min()*3>=2*D and mass@weights==D:
   print('CERT',[(sym[i] if i<4 else orbits[i-4],int(w)) for i,w in enumerate(weights) if w]);break
