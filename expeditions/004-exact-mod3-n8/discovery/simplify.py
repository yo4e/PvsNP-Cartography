from pathlib import Path
from fractions import Fraction as F
import numpy as np, json
from scipy.optimize import milp, LinearConstraint, Bounds
D=Path(__file__).parent
p=json.loads((D/'search_profiles.json').read_text()); cnt=np.array([a[1] for a in p]); sz=np.array([1,8,28,56,70,56,28,8,1]); A=cnt/sz
# Pair search: exact success constraints checked again after discovery.
for i in range(len(A)):
 diff=A[i]-A;rhs=2/3-A
 lower=np.max(np.where(diff>1e-10,rhs/np.where(abs(diff)>1e-10,diff,1),-np.inf),axis=1)
 upper=np.min(np.where(diff< -1e-10,rhs/np.where(abs(diff)>1e-10,diff,1),np.inf),axis=1)
 okay=np.all((abs(diff)>1e-10)|(rhs<=1e-10),axis=1)&(np.maximum(lower,0)<=np.minimum(upper,1)+1e-10)
 if np.any(okay):
  j=np.nonzero(okay)[0][0];print('PAIR',p[i],p[j],lower[j],upper[j]);break
else:
 print('NO PAIR in searched pool')
 # Integer multiples of 1/12; min total support using binary indicators.
 m=len(A); den=12
 M=np.zeros((10+2*m,2*m))
 M[0,:m]=1;M[1:10,:m]=cnt.T*3
 M[10:10+m,:m]=np.eye(m);M[10:10+m,m:]=-den*np.eye(m)
 M[10+m:,:m]=np.eye(m);M[10+m:,m:]=-np.eye(m)
 lo=np.r_[den,2*den*sz,np.full(m,-np.inf),np.zeros(m)]
 hi=np.r_[den,np.full(9,np.inf),np.zeros(m),np.full(m,np.inf)]
 r=milp(np.r_[np.zeros(m),np.ones(m)],integrality=np.ones(2*m),bounds=Bounds(np.zeros(2*m),np.r_[np.full(m,den),np.ones(m)]),constraints=LinearConstraint(M,lo,hi),options={'time_limit':15,'mip_rel_gap':0.0})
 print('MILP',r.message, r.fun)
 if r.x is not None:
  vals=[(int(round(r.x[i])),p[i]) for i in range(m) if r.x[i]>.5]
  print(vals)
  assert sum(w for w,a in vals)==den
  exact=[sum(F(w,den)*F(a[1][k],int(sz[k])) for w,a in vals) for k in range(9)]
  print('EXACT',list(map(str,exact)), 'MIN',min(exact))
  assert min(exact)>=F(2,3)
  (D/'compact_candidate.json').write_text(json.dumps({'denominator':den,'rows':vals,'success':list(map(str,exact))},indent=2))
