import math
from collections import Counter
from orb import fac
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
import pickle
reps=[r for r in pickle.load(open('cl6.pkl','rb')) if r>1]
BM=[2**p-1 for p in [13,17,19,31,61,89]]
tot=hit=0; V=Counter()
for n in reps:
    x=n
    while x<10**30:
        if x>n*10**6:
            tot+=1; hit+=any(x%m==0 for m in BM); V[(x&-x).bit_length()-1]+=1
        x=sig(x)
print('baseline points',tot,'divisible by big Mersenne %.1f%%'%(100*hit/tot))
s=sum(V.values()); print('baseline v2 dist %:',[(k,round(100*v/s,1)) for k,v in sorted(V.items()) if v/s>0.01])
