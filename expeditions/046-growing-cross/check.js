"use strict";
function expedition046() {
  const check=(x,m)=>{if(!x)throw Error(m)};
  const pc=x=>{let n=0;while(x){x&=x-1;n++}return n};
  const pop=x=>{let n=0;while(x){x&=x-1n;n++}return n};
  const pow2=x=>2**Math.ceil(Math.log2(Math.max(1,x)));
  const lg=x=>Math.ceil(Math.log2(Math.max(1,x)));
  const arr=n=>Array.from({length:n},(_,i)=>i);
  function build(a,mod,no) {
    const k=2*a+1,s=2**a,N=2**k,L=2*k,theta=N,D0=3*N,f=3*s-3;
    const FULL=(1n<<BigInt(N))-1n;
    const bm=(x,y)=>{let r=0;while(y){if(y&1)r^=x;y>>>=1;x<<=1;if(x&N)x^=mod}return r};
    // Verify the given base modulus by absence of zero divisors via inverses.
    function power(x,n,mul){let r=1;while(n){if(n&1)r=mul(r,x);x=mul(x,x);n=Math.floor(n/2)}return r}
    for(let x=1;x<N;x++)check(bm(x,power(x,N-2,bm))===1,"base field");
    const mul=(x,y)=>{let p=x&(N-1),q=x>>k,r=y&(N-1),t=y>>k;
      let ac=bm(p,r),bd=bm(q,t);return (ac^bd)|((bm(p^q,r^t)^ac)<<k)};
    const inv=x=>{check(x!==0,"inverse zero");let r=power(x,N*N-2,mul);check(mul(x,r)===1,"extension inverse");return r};
    const times=(p,x)=>{let r=Array(p.length+1).fill(0);for(let i=0;i<p.length;i++){r[i]^=mul(p[i],x);r[i+1]^=p[i]}return r};
    const van=xs=>xs.reduce(times,[1]);
    const ev=(p,x)=>p.reduceRight((v,c)=>mul(v,x)^c,0);
    const q=van(arr(s)), ys=arr(2*s).map(v=>ev(q,v*s));
    check(new Set(ys).size===2*s,"distinct ordinates");
    const ext=p=>{let r=0;for(let j=0;j<a-1;j++)if(p>>j&1)r^=(2**(j+2))*N;return r};
    const point=(v,p,u)=>(p<s/2?v*s:D0)^ext(p)^u;
    const weights=(nodes,x)=>nodes.map((v,i)=>{let n=1,d=1;for(let j=0;j<nodes.length;j++)if(j!==i){n=mul(n,x^nodes[j]);d=mul(d,v^nodes[j])}return mul(n,inv(d))});
    const basis=arr(s).map(i=>{let p=van(arr(s).filter(j=>j!==i)),t=inv(ev(p,i));return p.map(c=>mul(c,t))});
    const cw=arr(2*s).map(v=>weights(ys.slice(0,2),ys[v]));
    let size=1,inputs=new Map([["one",1]]),gates=[],memo=new Map(),scales=new Map();
    function inp(key){if(!inputs.has(key))inputs.set(key,++size);return inputs.get(key)}
    const x=arr(k).map(i=>inp("z:"+i));
    function gate(op,u,v){
      if(op==="and"){if(u===-1||v===-1||u===-v)return -1;if(u===1||u===v)return v;if(v===1)return u}
      else {if(u===v)return -1;if(u===-v)return 1;if(Math.abs(u)===1)return u===1?-v:v;if(Math.abs(v)===1)return v===1?-u:u}
      if(u>v)[u,v]=[v,u];let key=op+":"+u+":"+v;
      if(!memo.has(key)){memo.set(key,++size);gates.push([op,u,v,size])}
      return memo.get(key)
    }
    const parity=ls=>ls.reduce((u,v)=>gate("xor",u,v),-1);
    const add=(...ws)=>ws[0].map((_,i)=>parity(ws.map(w=>w[i])));
    const con=(v,n)=>arr(n).map(i=>(v>>i&1)?1:-1);
    const read=(b,p,d,n)=>arr(n).map(i=>i<(p===0?k:L)?inp([b,p,i,d].join(":")):-1);
    function scale(w,c){
      let key=w.length+":"+c,im=scales.get(key);
      if(!im){im=arr(w.length).map(i=>mul(1<<i,c));scales.set(key,im)}
      return arr(w.length).map(i=>parity(w.filter((_,j)=>im[j]>>i&1)))
    }
    function prod(u,v){
      let ts=arr(u.length).map(()=>[]);
      for(let i=0;i<u.length;i++)for(let j=0;j<v.length;j++){
        let w=gate("and",u[i],v[j]),m=mul(1<<i,1<<j);
        for(let h=0;h<u.length;h++)if(m>>h&1)ts[h].push(w)
      }return ts.map(parity)
    }
    const lin=(ws,cs)=>add(...ws.map((w,i)=>scale(w,cs[i])));
    function translate(co,shift,guard=0){let r=co.slice(),p=shift;
      for(let bit=1;bit<s;bit*=2){for(let i=0;i<s;i++)if(i&bit){
        let t=scale(r[i],p);if(guard)t=t.map(w=>gate("and",guard,w));r[i^bit]=add(r[i^bit],t)
      }p=mul(p,p)}return r
    }
    const ds=[...arr(s),...arr(2*s).slice(1).map(v=>v*s)];
    const A=new Map(ds.map(d=>[d,read("A",0,d,k)])),B=read("B",0,0,k);
    const zp=ts=>ts.map(t=>add(x,con(t,k))).reduce(prod);
    const triple=(u,v,w)=>prod(prod(u,v),w);
    const u=add(A.get(0),con(1,k)),v=add(A.get(no?0:1),con(1,k)),w=A.get(no?1:0);
    const bad=add(prod(zp([1,2,3]),triple(u,u,v)),prod(zp([0,2,3]),triple(w,w,w)),
      prod(zp([0,1]),prod(A.get(2),add(A.get(2),con(1,k)))),prod(zp([0,1,2,3]),B));
    const residualGateCount=gates.length;
    const slope=add(A.get(0),A.get(1));
    for(const d of ds.slice(2))bad.push(...add(A.get(d),A.get(0),scale(slope,d)));
    const parent=arr(s).map(j=>read("B",0,j,L));
    const co=arr(s).map(i=>lin(parent,basis.map(b=>b[i])));
    let rect=translate(co,D0);
    for(let j=a;j<k;j++)rect=translate(rect,1<<j,x[j]);
    for(let p=1;p<s;p++)for(let j=0;j<s;j++){
      let t=ext(p)^j,ps=[1];while(ps.length<s)ps.push(mul(ps[ps.length-1],t));
      bad.push(...add(lin(p<s/2?co:rect,ps),read("B",p,j,L)))
    }
    for(let p=s/2;p<s;p++){
      let ws=[read("B",p,0,L),read("B",p,s,L)];
      for(let v=2;v<2*s;v++)bad.push(...add(lin(ws,cw[v]),read("B",p,v*s,L)))
    }
    const output=bad.reduce((u,v)=>gate("and",u,-v),1);
    // Physically deduplicate fields; build actual copy chains with demand slots.
    let tags=[],keys=new Map(),loc=Array(size+1),raw=new Map(),readers=new Map();
    function tag(key){if(!keys.has(key)){keys.set(key,tags.length);tags.push(key)}return keys.get(key)}
    for(const [key,i] of inputs){let p=key.split(":");
      if(p[0]==="A"||p[0]==="B"){let base=p.slice(0,3).join(":"),t=tag(base),d=+p[3];raw.set(i,[t,d]);readers.set(t,(readers.get(t)||0)+1)}
    }
    for(let i=1;i<=size;i++)if(!raw.has(i))loc[i]=tag("private:"+i);
    const demand=Array(size+1).fill(0);
    for(const [,u,v] of gates){demand[Math.abs(u)]++;demand[Math.abs(v)]++}demand[Math.abs(output)]++;
    const copies=[],slots=Array(size+1),copyOf=[];
    // Literal representation [tag,delta,neg]; all output/copy rows local.
    const lit=(t,d=0,neg=false)=>[t,d,neg];
    for(let i=1;i<=size;i++){
      if(raw.has(i)){let [t,d]=raw.get(i);loc[i]=tag("buffer:"+i);copies.push([lit(t,d),loc[i]]);copyOf.push([loc[i],i])}
      let root=loc[i],d=demand[i],ls=[];
      while(d>f){ls.push(...Array(f-1).fill(root));let newt=tag("copy:"+i+":"+ls.length);copies.push([lit(root),newt]);copyOf.push([newt,i]);root=newt;d-=f-1}
      ls.push(...Array(d).fill(root));slots[i]=ls.reverse()
    }
    function use(w){let t=slots[Math.abs(w)].pop();check(t!==undefined,"demand");return lit(t,0,w<0)}
    const defs=gates.map(([op,u,v,i])=>[op,use(u),use(v),loc[i]]),out=use(output);
    check(slots.slice(1).every(ls=>ls.length===0),"unused demand");
    const loads=Array(tags.length).fill(0);
    for(const [,u,v] of defs){loads[u[0]]++;loads[v[0]]++}
    for(const [u] of copies)loads[u[0]]++;loads[out[0]]++;
    let rawTags=new Set([...raw.values()].map(x=>x[0]));
    const mu=Math.max(...readers.values());check(mu===3*s-1,"reader load");
    check(loads.every((d,t)=>d<=(rawTags.has(t)?mu:f)),"actual fanout");
    const PUB=arr(k).map(i=>arr(N).reduce((v,z)=>v|((z>>i&1)?1n<<BigInt(z):0n),0n));
    function shift(w,d){for(let i=0;i<k;i++)if(d>>i&1){let b=BigInt(1<<i);w=((w&PUB[i])>>b)|((w&(FULL^PUB[i]))<<b)}return w}
    function honest(coeff){let p=coeff.slice();while(p.length<2*s)p.push(0);let S=Array(s).fill(0);
      for(let i=s-1;i>=0;i--){S[i]=p[i+s];for(let j=0;j<=s;j++)p[i+j]^=mul(S[i],q[j])}
      const R=p.slice(0,s);return arr(s).map(p=>arr(N).map(z=>{let v=z>>a,t=point(v,p,z&(s-1));return ev(R,t)^mul(ys[v],ev(S,t))}))
    }
    function pack(A,B){
      let rows=Array(tags.length).fill(0n),vals=Array(size+1).fill(0n);vals[1]=FULL;rows[loc[1]]=FULL;
      for(let i=0;i<k;i++)vals[x[i]]=rows[loc[x[i]]]=PUB[i];
      for(const [key,t] of keys){let [b,p,j]=key.split(":");if(b!=="A"&&b!=="B")continue;
        let ws=b==="A"?A:B[+p];rows[t]=ws.reduce((m,v,z)=>m|((v>>+j&1)?1n<<BigInt(z):0n),0n)}
      for(const [i,[t,d]] of raw)vals[i]=shift(rows[t],d);
      const val=w=>w>0?vals[w]:FULL^vals[-w];
      for(const [op,u,v,i] of gates){let m=op==="xor"?val(u)^val(v):val(u)&val(v);vals[i]=rows[loc[i]]=m}
      for(const [t,i] of copyOf)rows[t]=vals[i];
      return rows
    }
    const readLit=(rows,[t,d,neg])=>shift(rows[t],d)^(neg?FULL:0n);
    function failures(rows){
      let n=pop(FULL^rows[loc[1]])+pop(FULL^readLit(rows,out));
      for(let i=0;i<k;i++)n+=2*pop(rows[loc[x[i]]]^PUB[i]);
      for(const [u,t] of copies)n+=pop(readLit(rows,u)^rows[t]);
      for(const [op,u,v,t] of defs){let A=readLit(rows,u),B=readLit(rows,v),C=rows[t];
        n+=op==="xor"?pop(A^B^C):pop(C&(FULL^A))+pop(C&(FULL^B))+pop((FULL^C)&A&B)}
      return n
    }
    function fieldCheck(A,B){
      // Absolute-point interpolation, independently of circuit interpolation/translation.
      let goodRow=arr(2*s).map(v=>{
        let nodes=arr(s).map(j=>point(v,0,j)),vs=arr(s).map(j=>B[0][v*s+j]);
        // Reconstruct absolute polynomial, not by the circuit's translated basis.
        let co=Array(s).fill(0);
        for(let i=0;i<s;i++){let b=van(nodes.filter((_,j)=>j!==i)),c=mul(vs[i],inv(ev(b,nodes[i])));for(let j=0;j<s;j++)co[j]^=mul(b[j],c)}
        for(let p=1;p<s;p++)for(let j=0;j<s;j++)if(ev(co,point(v,p,j))!==B[p][v*s+j])return false;return true
      });
      let groups=arr(s).map(j=>{for(let p=s/2;p<s;p++){
        let b0=B[p][j],b1=B[p][s+j],m=mul(b0^b1,inv(ys[0]^ys[1]));
        for(let v=2;v<2*s;v++)if((b0^mul(m,ys[v]^ys[0]))!==B[p][v*s+j])return false}return true});
      let n=0;
      for(let z=0;z<N;z++){
        let m=A[z]^A[z^1];
        if(!goodRow[z>>a]||!groups[z&(s-1)]||ds.some(d=>(A[z^d]^A[z])!==mul(d,m))){n++;continue}
        const zp=ts=>ts.reduce((r,t)=>mul(r,z^t),1),t=A[z]^1,h=A[z^(no?0:1)]^1,b=A[z^(no?1:0)],c=A[z^2];
        let r=mul(zp([1,2,3]),mul(mul(t,t),h))^mul(zp([0,2,3]),mul(mul(b,b),b))^mul(zp([0,1]),mul(c,c^1))^mul(zp([0,1,2,3]),B[0][z]);
        if(r)n++
      }return n
    }
    const A0=arr(N).map(z=>no?0:z^1);
    let W=van(arr(2*s).map(i=>i+4)),B0=honest(no?W.slice(1).map(c=>mul(c,inv(W[0]))):[0,1]);
    let rows=pack(A0,B0),V=N-2*s-3,expected=no?V:0;
    check(failures(rows)===expected&&fieldCheck(A0,B0)===expected,"honest failure");
    // Honest interpolation of each parent inverse row, but no global B polynomial.
    const inverseRoot=arr(N).map(z=>z?inv(z):0);
    const row0=arr(s).map(i=>arr(s).reduce((r,j)=>r^mul(basis[j][i],inverseRoot[j]),0));
    const invPolys=arr(2*s).map(v=>v?q.slice(1).map(c=>mul(c,inv(ys[v]))):row0);
    const inverseRows=arr(s).map(p=>arr(N).map(z=>ev(invPolys[z>>a],point(z>>a,p,z&(s-1)))));
    check(inverseRows[0].every((v,z)=>v===inverseRoot[z]),"inverse row roots");
    check(fieldCheck(Array(N).fill(0),inverseRows)===N,"shared sibling attack");
    let attacks=[];
    for(const [name,A,B] of [
      ["inverse-interpolated-rows",Array(N).fill(0),inverseRows],
      ["A-splice",A0.map((z,i)=>i>=N/2?z^1:z),B0],
      ["B-root",A0,B0.map((p,i)=>i?p:p.map((v,j)=>j===N-1?v^1:v))],
      ["B-common",A0,B0.map((p,i)=>i===s/2?p.map((v,j)=>j===0?v^1:v):p)],
      ["inverse-detached",Array(N).fill(0),arr(s).map(p=>arr(N).map(z=>p||!z?0:inv(z)))]
    ]){let direct=fieldCheck(A,B),actual=failures(pack(A,B));check(direct===actual,"scalar attack "+name);if(no)check(actual>=V,"NO attack");attacks.push([name,actual])}
    // Actual physical singleton and mixed mutations, including clamped pins.
    if(!no){
      let t=keys.get("A:0:0"),w=rows[t];rows[t]^=1n;check(failures(rows)===mu,"attaining raw singleton");rows[t]=w;
      let t2=loc[x[0]],w2=rows[t2];rows[t2]^=1n;rows[t]^=1n;let mixed=failures(rows);check(mixed<=2*mu,"mixed");rows[t2]=w2;rows[t]=w;attacks.push(["raw-plus-pin",mixed])
    }
    let G=gates.length,C=copies.length,And=gates.filter(g=>g[0]==="and").length,Xor=G-And,R=tags.length,Q=N*pow2(R);
    let M=3*And+4*Xor+2*C+2+2*k;
    let result={a,k,N,no,And,Xor,C,R,Q,M,mu,V,guaranteedErrors:Math.floor((V-1)/mu),attacks,residualGateCount};
    if(no)return {result,rows:null};
    // Exact row ANF, then coefficient-tag completion; copies of identical nonlinear rows share a signature, never a physical location.
    function anf(w){for(let i=0;i<k;i++)w^=(w&(FULL^PUB[i]))<<BigInt(1<<i);return w}
    const masks=arr(k+1).map(d=>arr(N).reduce((r,z)=>r|(pc(z)===d?1n<<BigInt(z):0n),0n));
    const degree=w=>{for(let d=k;d>=0;d--)if(w&masks[d])return d;return 0};
    let affineMask=1n;for(let i=0;i<k;i++)affineMask|=1n<<BigInt(1<<i);
    let Acounts=new Map(),Ecounts=new Map(),exceptional=[],maxSeedDegree=0,maxAffine=0,maxExc=0,nonlinear=0,allocation=[];
    const cache=new Map();
    for(let t=0;t<R;t++){
      let w=rows[t],c=cache.get(w);if(c===undefined){c=anf(w);cache.set(w,c)}
      maxSeedDegree=Math.max(maxSeedDegree,degree(c));
      if(!(c&~affineMask)){
        let sig=Number(c&1n);for(let i=0;i<k;i++)if(c&(1n<<BigInt(1<<i)))sig|=1<<(i+1);
        let rank=Acounts.get(sig)||0;Acounts.set(sig,rank+1);maxAffine=Math.max(maxAffine,rank+1);allocation.push([0,sig,rank]);
      }else{
        nonlinear++;let data=Ecounts.get(w);if(!data){data=[exceptional.length,0];exceptional.push(w);Ecounts.set(w,data)}
        let rank=data[1]++;maxExc=Math.max(maxExc,rank+1);allocation.push([1,data[0],rank])
      }
    }
    // Algebraic checks: nonlinear truth rows can only originate in the outer residual gates.
    check(exceptional.length<=residualGateCount,"nonlinear source count");
    const h=Math.max(k+1,lg(exceptional.length)),r=lg(Math.max(maxAffine,maxExc));
    let codeQ=N*2*2**(h+r),seen=new Set();
    for(let t=0;t<R;t++){
      let [b,sig,rank]=allocation[t],addr=(b*2**(h+r)+rank*2**h+sig);
      check(!seen.has(addr),"collision");seen.add(addr);
      let expect=b?exceptional[sig]:(sig&1?FULL:0n);
      if(!b)for(let i=0;i<k;i++)if(sig>>(i+1)&1)expect^=PUB[i];
      check(expect===rows[t],"tag polynomial mismatch")
    }
    const E=arr(pow2(exceptional.length)).map(i=>exceptional[i]||0n);
    for(let bit=1;bit<E.length;bit*=2)for(let i=0;i<E.length;i++)if(i&bit)E[i]^=E[i^bit];
    let de=0;for(let i=0;i<E.length;i++)if(E[i])de=Math.max(de,pc(i)+degree(anf(E[i])));
    check(de>2,"branch degree");
    // Contiguous-prefix minimum exact completion: tag Möbius then seed Möbius; ignore all outside prefix.
    let tr=rows.slice();for(let b=1;b<R;b*=2)for(let i=0;i<R;i++)if(i&b)tr[i]^=tr[i^b];
    let compactDegree=0;for(let i=0;i<R;i++)if(tr[i])compactDegree=Math.max(compactDegree,pc(i)+degree(anf(tr[i])));
    result.layout={nonlinearRows:nonlinear,distinctNonlinear:exceptional.length,distinctAffine:Acounts.size,maxAffine,maxExc,maxSeedDegree,h,r,codeQ,exactCompletionDegree:de+1,compactMinimumExactDegree:compactDegree,
      rawErrorBudget:V+"/"+mu,structuredErrorDenominator:codeQ*mu,compactErrorDenominator:Q*mu,
      fixedCompletionLowerDegreeDistance:codeQ/2**(de+1)};
    // Separate the highly repeated constants from affine and exceptional rows.
    const maxConstant=Math.max(Acounts.get(0)||0,Acounts.get(1)||0);
    const maxOther=Math.max(1,...[...Acounts].filter(([sig])=>sig>1).map(([,n])=>n));
    const cBits=1+lg(maxConstant),aBits=k+1+lg(maxOther),eBits=lg(exceptional.length)+lg(maxExc);
    const tBits=Math.max(cBits,aBits,eBits),bankSize=2**tBits,bankQ=4*N*bankSize;
    const occupied=new Set();
    for(let t=0;t<R;t++){
      const [b,sig,rank]=allocation[t];
      let bank=b?2:sig<=1?0:1;
      let bits=bank===0?1:bank===1?k+1:lg(exceptional.length);
      let addr=bank*bankSize+rank*2**bits+sig;
      check(addr<(bank+1)*bankSize&&!occupied.has(addr),"separated banks");
      occupied.add(addr);
      let value=bank===2?exceptional[sig]:sig&1?FULL:0n;
      if(bank===1)for(let i=0;i<k;i++)if(sig>>(i+1)&1)value^=PUB[i];
      check(value===rows[t],"bank completion");
    }
    // Full occupied half-cube (largest complete initial tag block).
    const T=2**Math.floor(Math.log2(R));
    let fixedDegree=0;
    for(let i=0;i<T;i++)if(tr[i])fixedDegree=Math.max(fixedDegree,pc(i)+degree(anf(tr[i])));
    const fixedDistance=T*N/2**fixedDegree;
    // Direct parity certificate, without evaluating any transformed truth values.
    let leadTag=-1,leadSeed=-1;
    for(let i=0;i<T&&leadTag<0;i++)if(tr[i]){
      let d=fixedDegree-pc(i);
      if(d>=0&&d<=k){let c=anf(tr[i])&masks[d];if(c){
        leadTag=i;for(let j=0;j<N;j++)if(c&(1n<<BigInt(j))){leadSeed=j;break}
      }}
    }
    check(leadTag>=0&&leadSeed>=0,"leading coefficient");
    const submasks=m=>{let out=[];for(let x=m;;x=(x-1)&m){out.push(x);if(!x)return out}};
    let parities=0;
    for(const base of submasks((T-1)^leadTag)){
      let w=0n;for(const h of submasks(leadTag))w^=rows[base|h];
      for(const z of submasks((N-1)^leadSeed)){
        let p=0;for(const h of submasks(leadSeed))p^=Number((w>>BigInt(z|h))&1n);
        check(p===1,"direct disjoint odd parity");parities++;
      }
    }
    check(parities===fixedDistance,"parity partition count");
    // Bank 3 is filled with E, so the nonlinear branch uses only one selector.
    const bankDegree=de+1;
    check(bankDegree>4,"dominant exceptional degree");
    Object.assign(result.layout,{maxConstant,maxOther,cBits,aBits,eBits,tBits,bankQ,bankDegree,
      bankErrorDenominator:bankQ*mu,bankFixedCompletionLowerDegreeDistance:bankQ/2**bankDegree,
      compactFixedPrefixRows:T,compactFixedPrefixDegree:fixedDegree,compactLowerDegreeDistance:fixedDistance,
      compactBudgetMinimumCertified:fixedDegree===compactDegree&&fixedDistance*mu>=V,parityLeadTag:leadTag,parityLeadSeed:leadSeed,directOddParityCubes:parities});
    // Unequal prefix banks: 0 = zero, 100 = light affine,
    // 101 = heavy affine (dense lookup), 11 = exceptional.
    const zeroCount=Acounts.get(0)||0;
    const nonzero=[...Acounts].filter(([sig])=>sig!==0).sort((u,v)=>u[0]-v[0]);
    let best=null;
    for(const limit of [0,...new Set(nonzero.map(([,n])=>n))]){
      let heavy=nonzero.filter(([,n])=>n>limit),light=nonzero.filter(([,n])=>n<=limit);
      let lbits=k+1+lg(Math.max(1,...light.map(([,n])=>n)));
      let hbits=lg(heavy.length)+lg(Math.max(1,...heavy.map(([,n])=>n)));
      let total=Math.max(lg(zeroCount)+1,lbits+3,hbits+3,eBits+2,3);
      let ub=Math.max(5,lg(heavy.length)+4,de+2);
      if(!best||total<best.total||(total===best.total&&ub<best.ub))
        best={limit,heavy,light,total,ub,lbits,hbits}
    }
    const heavyIndex=new Map(best.heavy.map(([sig],i)=>[sig,i]));
    let heavyTruth=arr(pow2(best.heavy.length)).map(i=>{
      let sig=best.heavy[i]?.[0]||0,w=sig&1?FULL:0n;
      for(let j=0;j<k;j++)if(sig>>(j+1)&1)w^=PUB[j];return w});
    let ht=heavyTruth.slice();
    for(let bit=1;bit<ht.length;bit*=2)for(let i=0;i<ht.length;i++)if(i&bit)ht[i]^=ht[i^bit];
    let hd=0;for(let i=0;i<ht.length;i++)if(ht[i])hd=Math.max(hd,pc(i)+degree(anf(ht[i])));
    let prefixQ=N*2**best.total,prefixDegree=Math.max(5,hd+3,de+2);
    let base0=2**(best.total-1),base1=base0+2**(best.total-3),base2=base0+2**(best.total-2);
    let tagMap=[],seen2=new Set();
    for(let t=0;t<R;t++){
      const [b,sig,rank]=allocation[t];let addr,value,upper;
      if(b){addr=base2+rank*2**lg(exceptional.length)+sig;value=exceptional[sig];upper=2**best.total}
      else if(!sig){addr=rank;value=0n;upper=base0}
      else if(heavyIndex.has(sig)){let i=heavyIndex.get(sig);addr=base1+rank*2**lg(best.heavy.length)+i;value=heavyTruth[i];upper=base2}
      else{addr=base0+rank*2**(k+1)+sig;value=sig&1?FULL:0n;
        for(let j=0;j<k;j++)if(sig>>(j+1)&1)value^=PUB[j];upper=base1}
      check(addr<upper&&!seen2.has(addr)&&value===rows[t],"unequal prefix layout");
      tagMap.push(addr);seen2.add(addr)
    }
    // Check the same literal/seed projection constraints on an actual reindexed proof.
    function mappedFailures(rows){
      const tab=new Map(tagMap.map((tag,i)=>[tag,rows[i]]));
      const get=t=>tab.get(tagMap[t]);
      const val=([t,d,neg])=>shift(get(t),d)^(neg?FULL:0n);
      let n=pop(FULL^get(loc[1]))+pop(FULL^val(out));
      for(let i=0;i<k;i++)n+=2*pop(get(loc[x[i]])^PUB[i]);
      for(const [u,t] of copies)n+=pop(val(u)^get(t));
      for(const [op,u,v,t] of defs){let A=val(u),B=val(v),C=get(t);
        n+=op==="xor"?pop(A^B^C):pop(C&(FULL^A))+pop(C&(FULL^B))+pop((FULL^C)&A&B)}
      return n
    }
    check(mappedFailures(rows)===0,"mapped honest proof");
    let mut=keys.get("A:0:0"),old=rows[mut];rows[mut]^=1n;
    check(mappedFailures(rows)===mu,"mapped singleton");rows[mut]=old;
    // Independent physical accounting identity and upper bound.
    check(rawTags.size===2*s*k&&raw.size===k*(4*s*s+s-1),"raw census formula");
    check(R===2*s*k+k+1+G+C,"row census formula");
    Object.assign(result.layout,{zeroCount,heavyThreshold:best.limit,heavyTypes:best.heavy.length,lightTypes:best.light.length,
      heavyDegree:hd,prefixTagBits:best.total,prefixQ,prefixDegreeUpper:prefixDegree,
      prefixErrorDenominator:prefixQ*mu,prefixSizeFactor:prefixQ/Q});
    return {result,rows:null}
  }
  // x^7+x+1 and x^9+x^4+1; verify field inverses in the build.
  // Separate literal-level truth-table audit of failure and charging formulas.
  let gateChecks=0;
  for(const op of ["and","xor","copy"]){
    const arity=op==="copy"?2:3;
    const clauses=op==="and"?[[-1,-2,3],[1,-3],[2,-3]]:
      op==="xor"?[[1,2,-3],[1,-2,3],[-1,2,3],[-1,-2,-3]]:[[-1,2],[1,-2]];
    for(let v=0;v<2**arity;v++){
      let x=v&1,y=v>>1&1,z=v>>2&1;
      let exact=clauses.filter(c=>!c.some(l=>Boolean(v>>(Math.abs(l)-1)&1)===(l>0))).length;
      let formula=op==="and"?z*(2-x-y)+(1-z)*x*y:op==="xor"?x^y^z:x^y;
      check(exact===formula,"literal failure formula");
      for(let w=0;w<2**arity;w++){
        let u=w&1,t=w>>1&1,h=w>>2&1;
        if((op==="and"?u&t:op==="xor"?u^t:u)!==(op==="copy"?t:h))continue;
        let e=x^u,f=y^t,g=z^h;
        check(exact<=e+f+(op==="and"?2*g:g),"all-error gate charge");
        gateChecks++;
      }
    }
  }
  // Fixed-layout counting attack on eight independently variable constant rows.
  let covered=new Set(),coveredExact=new Set();
  for(let c=0;c<16;c++){
    let w=0;for(let z=0;z<8;z++)if((c&1)^((pc((c>>1)&z))&1))w|=1<<z;
    coveredExact.add(w);covered.add(w);for(let i=0;i<8;i++)covered.add(w^(1<<i))
  }
  check(coveredExact.size===16&&covered.size===144,"fixed layout obstruction");
  const fixtures=[[3,0x83],[4,0x211]].map(([a,p])=>[build(a,p,false).result,build(a,p,true).result]);
  for(const [y,n] of fixtures){
    check(n.Q<=y.layout.bankQ&&n.Q<=y.layout.prefixQ,"common padded cube");
    check(y.layout.compactBudgetMinimumCertified,"compact budget optimum");
  }
  return {fixtures,gateChecks,fixedLayoutCountingControl:{rows:8,degreeOneTables:coveredExact.size,radiusOneCovered:covered.size,uncovered:256-covered.size}};
}
console.log(JSON.stringify(expedition046(),null,2));
