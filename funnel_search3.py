import random, math, sys, itertools
import numpy as np
W=(math.log(2),math.log(3),math.log(5))
def w(u): return u[0]*W[0]+u[1]*W[1]+u[2]*W[2]
def ent(): 
    r=random.random(); return 0 if r<.5 else 1 if r<.8 else 2 if r<.95 else 3
def mk(e,v):
    def T(u):
        out=[0,0,0]
        for i in range(3):
            a=u[i]
            if a:
                for j in range(3): out[j]+=e[i][j]+(a-1)*v[i][j]
        return tuple(out)
    return T
grid=[u for u in itertools.product(range(7),repeat=3) if any(u)]
starts=[u for u in itertools.product(range(4),repeat=3) if any(u)]
random.seed(int(sys.argv[2])); N=int(sys.argv[1])
stats={'nonexp':0,'disc':0,'conn_funnel':0,'conn_nofunnel':0,'complex':0,'complex_conn':0}; bad=[]
for it in range(N):
    e=[[ent() for _ in range(3)] for _ in range(3)]; v=[[ent() for _ in range(3)] for _ in range(3)]
    if not all(any(r) for r in e) or not all(any(r) for r in v): continue
    T=mk(e,v)
    if any(w(T(u))<=w(u)+1e-12 for u in grid): stats['nonexp']+=1; continue
    A=np.array(v).T; ev=np.linalg.eigvals(A); cplx=any(abs(z.imag)>1e-9 for z in ev)
    stats['complex']+=cplx
    seen={}; par=list(range(len(starts)))
    def f(i):
        while par[i]!=i: par[i]=par[par[i]]; i=par[i]
        return i
    for i,s in enumerate(starts):
        u=s
        while w(u)<150:
            if u in seen: par[f(i)]=f(seen[u]); break
            seen[u]=i; u=T(u)
    if len({f(i) for i in range(len(starts))})>1: stats['disc']+=1; continue
    stats['complex_conn']+=cplx
    u=(1,0,0); orb=[]
    while w(u)<150: orb.append(u); u=T(u)
    inc={tuple(orb[k+1][j]-orb[k][j] for j in range(3)) for k in range(len(orb)-8,len(orb)-1)}
    if len(inc)==1 and sorted(next(iter(inc)))==[0,0,1]: stats['conn_funnel']+=1
    else: stats['conn_nofunnel']+=1; bad.append((e,v,orb[-5:]))
print(stats); print(bad[:5])
