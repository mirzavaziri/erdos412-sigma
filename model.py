import sys, math, hashlib
from orb import fac, ip
def nextprime(q):
    q+=1
    while not ip(q): q+=1
    return q
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
def mkR(y):
    def F(n):
        v=sig(n); r={}; fac(v,r); out=1
        for q,e in r.items(): out*= (nextprime(q) if q>y else q)**e
        return out
    return F
def unif(n):
    h=int(hashlib.md5(str(n).encode()).hexdigest(),16)
    return n+1+h%n          # uniform in [n+1,2n]
def count(F,N,B):
    seen={}; reps=[]
    for n in range(2,N+1):
        x=n; new=True
        while x<B:
            if x in seen: new=False;break
            seen[x]=n; x=F(x)
        if new: reps.append(n)
    return reps
import bisect
which=sys.argv[1]; N=int(sys.argv[2])
F={'unif':unif}.get(which) or mkR(int(which))
reps=count(F,N,10**22)
print(which,[ (x,bisect.bisect_right(reps,x)) for x in [100,1000,10000,100000,1000000] if x<=N], reps[:15])
