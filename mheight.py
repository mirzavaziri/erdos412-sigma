import sys, math
from orb import fac
from collections import Counter
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
N=int(sys.argv[1]); B=10**30
seen={}; H=Counter(); R=Counter(); maxr=[]
for n in range(2,N+1):
    x=n;k=0
    while True:
        if x in seen:
            if k>0:
                H[int(math.log10(x))]+=1
                r=math.log10(x/n); R[int(r)]+=1
                if r>6: maxr.append((round(r,1),n,seen[x]))
            break
        if x>=B: break
        seen[x]=n; x=sig(x); k+=1
print('merge value decade:',sorted(H.items()))
print('log10(merge value / n):',sorted(R.items()))
print('largest ratios:',sorted(maxr)[-10:])
