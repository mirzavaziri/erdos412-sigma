import sys
from cls import classes, fac
from orb import fac
import math
def F2(n):
    r={};fac(n,r);s=1
    for p,e in r.items():
        t=min(e,2); s*=(p**(t+1)-1)//(p-1)*p**(e-t)
    return s
def psi(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=p**(e-1)*(p+1)
    return s
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
N=100000
cl=classes(F2,N,10**22); print('trunc-2 classes',len(cl))
cl=classes(psi,N,10**22)
def v3end(n):
    x=n
    for _ in range(60): x=psi(x)
    b=0
    while x%3==0: x//=3;b+=1
    return b
ok=all(len({v3end(n) for n in v[:20]})==1 for v in cl.values())
print('psi classes',len(cl),'invariant consistent',ok, sorted(v3end(min(v)) for v in cl.values()))
cl=classes(sig,N,10**22)
reps=sorted(min(v) for v in cl.values())
def sqish(n):
    r=math.isqrt(n); r2=math.isqrt(n//2)
    return r*r==n or (n%2==0 and r2*r2*2==n)
print('sigma reps',len(reps),'square or 2*square:',sum(map(sqish,reps)),'prime:',sum(1 for n in reps if len({0} if n<2 else (lambda d:d)( (lambda r:(fac(n,r),r)[1])({}) ))==1 and (lambda r:(fac(n,r),r)[1])({}).get(n,0)==1))
print(reps[:60])
