import sys,time
from cls import *
kind=sys.argv[1]; B=10**int(sys.argv[2]); N=int(sys.argv[3])
t=time.time(); cl=classes(mk(kind),N,B)
rep={}
for r,v in cl.items():
    for n in v: rep[n]=min(v)
# C(x): number of classes meeting [2,x], counted by min element
mins=sorted(min(v) for v in cl.values())
import bisect
out=[(x,bisect.bisect_right(mins,x)) for x in [10,100,1000,10000,100000,1000000] if x<=N]
print(kind,'B=1e%s'%sys.argv[2],'N=',N,'classes',len(cl),out,'%.0fs'%(time.time()-t))
