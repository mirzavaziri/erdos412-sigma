import sys, bisect
from orb import fac, ip
from functools import lru_cache
Y=1000
SKIP=int(sys.argv[3]) if len(sys.argv)>3 else 1
def smooth_succ(q):          # q+1 is Y-smooth
    m=q+1
    for p in range(2,Y+1):
        while m%p==0: m//=p
        if m==1: return True
    return m==1
def mersenne(q): return (q+1)&q==0
def mk(exempt):
    @lru_cache(maxsize=None)
    def g(q):
        if q<=Y or exempt(q): return q
        r=q;c=0
        while True:
            r+=1
            if ip(r) and not exempt(r):
                c+=1
                if c==SKIP: return r
    def F(n):
        r={};fac(n,r);v=1
        for p,e in r.items(): v*=(p**(e+1)-1)//(p-1)
        r={};fac(v,r);out=1
        for q,e in r.items(): out*=g(q)**e
        return out
    return F
def count(F,N,B=10**22):
    seen={};reps=[]
    for n in range(2,N+1):
        x=n;new=True
        while x<B:
            if x in seen:new=False;break
            seen[x]=n;x=F(x)
        if new:reps.append(n)
    return reps
if __name__=="__main__":
    w=sys.argv[1];N=int(sys.argv[2])
    ex={'mers':mersenne,'smooth':smooth_succ,'none':lambda q:False}[w]
    reps=count(mk(ex),N)
    print(w,[(x,bisect.bisect_right(reps,x)) for x in [10**3,10**4,10**5,10**6] if x<=N],flush=True)
    open('reps_%s_%d_%d.txt'%(w,N,SKIP),'w').write(' '.join(map(str,reps)))
