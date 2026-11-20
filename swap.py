import sys,bisect
from orb import fac, ip
from model2 import count
def nextprime(q):
    q+=1
    while not ip(q): q+=1
    return q
M=[2**p-1 for p in [13,17,19,31,61]]
SW={}
for m in M:
    r=nextprime(m); SW[m]=r; SW[r]=m
def F(n):
    r={};fac(n,r);v=1
    for p,e in r.items(): v*=(p**(e+1)-1)//(p-1)
    r={};fac(v,r);out=1
    for q,e in r.items(): out*=SW.get(q,q)**e
    return out
reps=count(F,int(sys.argv[1]))
print('swapM',[(x,bisect.bisect_right(reps,x)) for x in [10**3,10**4,10**5,10**6]],flush=True)
