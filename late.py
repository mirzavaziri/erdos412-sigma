import math
from collections import Counter
from orb import fac
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
N=10**6;B=10**30;seen={};V=Counter();MD=Counter();tot=0
MEXP=[2,3,5,7,13,17,19,31,61,89]
for n in range(2,N+1):
    x=n;k=0;prev=None
    while x<B:
        if x in seen:
            if k>0 and x>n*10**6:
                tot+=1; v=(x&-x).bit_length()-1; V[v]+=1
                # previous value (before merge) divisible by a big Mersenne prime?
                MD[any(prev%(2**p-1)==0 for p in [13,17,19,31,61,89])]+=1
            break
        seen[x]=n; prev=x; x=sig(x); k+=1
print('late merges',tot)
print('v2(merge value):',sorted(V.items()))
print('value just before merge divisible by big Mersenne prime:',dict(MD))
