import itertools, math
W=(math.log(2),math.log(3))
def mkT(e1,v1,e2,v2):
    def E(e,v,a): return (0,0) if a==0 else (e[0]+(a-1)*v[0], e[1]+(a-1)*v[1])
    def T(u):
        x=E(e1,v1,u[0]); y=E(e2,v2,u[1]); return (x[0]+y[0],x[1]+y[1])
    return T
def w(u): return u[0]*W[0]+u[1]*W[1]
import sys
vals=list(range(int(sys.argv[1])))
vecs=list(itertools.product(vals,repeat=2))
res={'conn_funnel':0,'conn_nofunnel':0,'disc':0,'nonexp':0}; bad=[]
G=[(a,b) for a in range(0,14) for b in range(0,14) if (a,b)!=(0,0)]
for e1,v1,e2,v2 in itertools.product(vecs,repeat=4):
    T=mkT(e1,v1,e2,v2)
    if any(w(T(u))<=w(u)+1e-12 for u in G): res['nonexp']+=1; continue
    starts=[(a,b) for a in range(0,7) for b in range(0,7) if (a,b)!=(0,0)]
    seen={}; par=list(range(len(starts)))
    def f(i):
        while par[i]!=i: par[i]=par[par[i]]; i=par[i]
        return i
    for i,s in enumerate(starts):
        u=s
        while w(u)<120:
            if u in seen: par[f(i)]=f(seen[u]); break
            seen[u]=i; u=T(u)
    k=len({f(i) for i in range(len(starts))})
    if k>1: res['disc']+=1; continue
    # funnel: tail increments of orbit of (1,0) equal a unit axis vector
    u=(1,0); orb=[]
    while w(u)<120: orb.append(u); u=T(u)
    inc={(orb[j+1][0]-orb[j][0],orb[j+1][1]-orb[j][1]) for j in range(len(orb)-8,len(orb)-1)}
    if inc in ({(1,0)},{(0,1)}): res['conn_funnel']+=1
    else: res['conn_nofunnel']+=1; bad.append((e1,v1,e2,v2,orb[-6:]))
print(res); print(bad[:10])
