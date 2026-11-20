import math
from orb import fac
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
BIG=[2**p-1 for p in [13,17,19,31,61]]
ALLM=[2**p-1 for p in [2,3,5,7]]+BIG
import pickle
reps=[r for r in pickle.load(open('cl6.pkl','rb')) if r>1]
for R in [10**3,10**6,10**9,10**12]:
    hit=0
    for n in reps:
        x=n
        while x< n*R:
            if any(x%m==0 for m in BIG): hit+=1;break
            x=sig(x)
    print('rep orbits up to ratio 1e%d: contain big Mersenne %.1f%%'%(len(str(R))-1,100*hit/len(reps)))
