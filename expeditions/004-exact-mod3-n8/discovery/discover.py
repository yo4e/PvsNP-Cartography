from pathlib import Path
from itertools import combinations
import numpy as np
from scipy.optimize import linprog
import subprocess, json, time
D=Path(__file__).parent
sizes=np.array([1,8,28,56,70,56,28,8,1])
rows={}
def insert(c,a,b):
 coef=c|(a<<1)|(b<<9)
 cnt=[0]*9
 for x in range(256):
  p=c^((a&x).bit_count()&1)
  for j,(v,w) in enumerate(combinations(range(8),2)):
   p^=((b>>j)&1)&((x>>v)&1)&((x>>w)&1)
  if p==int(x.bit_count()%3==0):cnt[x.bit_count()]+=1
 rows[tuple(cnt)]=coef
for c in (0,1):
 for a in (0,255):
  for b in (0,(1<<28)-1):insert(c,a,b)
insert(1,255,60548413)
trace=[]
for step in range(35):
 counts=np.array(list(rows)); A=counts/sizes; m=len(A)
 r=linprog(np.r_[np.zeros(m),-1.],A_ub=np.c_[-A.T,np.ones(9)],b_ub=np.zeros(9),A_eq=np.r_[np.ones(m),0][None],b_eq=[1],bounds=[(0,None)]*m+[(0,1)],method='highs')
 if not r.success:raise RuntimeError(r.message)
 q=-r.ineqlin.marginals
 v=-r.fun
 support=[dict(coef=int(rows[tuple(counts[i])]),counts=counts[i].tolist(),weight=float(r.x[i])) for i in range(m) if r.x[i]>1e-9]
 snap=dict(step=step,value=v,q=q.tolist(),support=support,num_profiles=m)
 trace.append(snap);print(step,m,v,'q',np.round(q,5),flush=True)
 (D/'search_progress.json').write_text(json.dumps(trace,indent=2))
 if v>=2/3-1e-10:
  print('CANDIDATE',json.dumps(snap,indent=2),flush=True);break
 p=subprocess.run([str(D/'search'),'2500',str(20261009+step)],input=' '.join(map(str,q)),text=True,capture_output=True,check=True)
 old=len(rows)
 for line in p.stdout.splitlines():
  nums=list(map(int,line.split()));rows[tuple(nums[1:])]=nums[0]
 if len(rows)==old:print('Heuristic stagnation',flush=True);break
(D/'search_profiles.json').write_text(json.dumps([[int(c),list(k)] for k,c in rows.items()]))
