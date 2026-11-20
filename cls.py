import sys, time
sys.setrecursionlimit(10000)
from orb import fac
def mk(kind):
    def F(n):
        r={};fac(n,r);s=1
        for p,e in r.items():
            if kind=='sigma': s*=(p**(e+1)-1)//(p-1)
            elif kind=='unitary': s*=p**e+1
            elif kind=='psi': s*=p**e+p**(e-1)   # Dedekind psi
            elif kind=='sqf': s*=(p+1)**e        # completely mult. p->p+1
        return s
    return F
def classes(F,N,B):
    par=list(range(N+1))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    seen={}; esc=0
    for n in range(2,N+1):
        x=n
        while True:
            if x in seen: 
                a,b=f(n),f(seen[x]); 
                if a!=b: par[max(a,b)]=min(a,b)
                break
            if x>=B: esc+=1; break
            seen[x]=n; x=F(x)
    cl={}
    for n in range(2,N+1): cl.setdefault(f(n),[]).append(n)
    return cl
