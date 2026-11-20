import sys, math, pickle
from orb import fac
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
N=int(sys.argv[1]); B=10**22
seen={}; step=[None]*(N+1)
for n in range(2,N+1):
    x=n;k=0
    while True:
        if x in seen: step[n]=k;break
        if x>=B: step[n]=-1;break
        seen[x]=n; x=sig(x); k+=1
pickle.dump(step,open('step%d.pkl'%N,'wb'))
# survival by dyadic blocks
for t in range(4,int(math.log2(N))+1):
    lo,hi=2**t,min(2**(t+1),N+1)
    blk=[step[n] for n in range(lo,hi)]
    m=len(blk)
    surv=[sum(1 for s in blk if s==-1 or s>k)/m for k in range(0,8)]
    print(t, m, ' '.join('%.4f'%v for v in surv), 'reps',sum(1 for s in blk if s==-1))
