import math
from orb import fac
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
BIG=[2**p-1 for p in [13,17,19,31,61]]
ALLM=[2**p-1 for p in [2,3,5,7]]+BIG
N=10**6;B=10**30;seen={}
stat={}  # bucket -> [count, withBIG, withALL]
for n in range(2,N+1):
    x=n;k=0;path=[]
    while x<B:
        if x in seen:
            if k>0:
                r=math.log10(x/n); b='0-1' if r<1 else ('1-3' if r<3 else ('3-6' if r<6 else '6+'))
                s=stat.setdefault(b,[0,0,0]); s[0]+=1
                s[1]+= any(v%m==0 for v in path for m in BIG)
                s[2]+= any(v%m==0 for v in path for m in ALLM)
            break
        seen[x]=n; path.append(x); x=sig(x); k+=1
for b in ['0-1','1-3','3-6','6+']:
    c,a1,a2=stat[b]; print(b,c,'via big Mersenne %.1f%%'%(100*a1/c),'via any Mersenne %.1f%%'%(100*a2/c))
