import pickle,sys
from cls import classes, mk
from collections import Counter
for N in [10**4,10**5,10**6]:
    cl=classes(mk('sigma'),N,10**22)
    s=sorted((len(v) for v in cl.values()),reverse=True)
    top=s[:5]; c=Counter(s)
    print(N,len(s),'top',[round(t/N,4) for t in top],'singletons',c[1],'size2',c[2],'size<=5',sum(c[i] for i in range(1,6)),'median',s[len(s)//2])
    if N==10**6: pickle.dump({min(v):len(v) for v in cl.values()},open('cl6.pkl','wb'))
