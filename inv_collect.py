import pickle
from orb import fac
N=10**6;B=10**30;H=10**10
seen={};nxt={};F={};owner={}
def sigf(x):
    r={};fac(x,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s,r
par=list(range(N+1))
def find(a):
    while par[a]!=a: par[a]=par[par[a]]; a=par[a]
    return a
for n in range(2,N+1):
    x=n
    while x<B:
        if x in seen:
            a,b=find(n),find(seen[x])
            if a!=b: par[max(a,b)]=min(a,b)
            break
        seen[x]=n; s,r=sigf(x)
        if x>H: F[x]=r; nxt[x]=s
        x=s
cls={x:find(seen[x]) for x in F}
pickle.dump((F,nxt,cls),open('inv.pkl','wb'))
print('points',len(F),'classes',len(set(cls.values())))
