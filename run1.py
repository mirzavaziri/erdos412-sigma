import sys,time
from cls import *
kind,N,B=sys.argv[1],int(sys.argv[2]),10**int(sys.argv[3])
t=time.time();cl=classes(mk(kind),N,B)
sz=sorted((len(v),min(v)) for v in cl.values())[::-1]
print(kind,N,'B=1e'+sys.argv[3],'classes:',len(cl),'time %.0fs'%(time.time()-t))
print('largest:',sz[:10]); print('reps(sorted):',sorted(m for _,m in sz)[:40])
