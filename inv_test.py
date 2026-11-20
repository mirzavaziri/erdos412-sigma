import pickle, itertools, math
from collections import defaultdict, Counter
F,nxt,cls=pickle.load(open('inv.pkl','rb'))
X=[x for x in F if nxt[x] in F]
def v(r,p): return r.get(p,0)
MEXP=[2,3,5,7,13,17,19,31,61,89]
feats={}
for m in [2,3,4,5,6,7,8,9,12,16,24,32]:
    feats['x mod %d'%m]=lambda x,r,m=m: x%m
    feats['odd part mod %d'%m]=lambda x,r,m=m: (x>>v(r,2))%m
for p in [2,3,5,7]:
    for m in [2,3,4,6]:
        feats['v%d mod %d'%(p,m)]=lambda x,r,p=p,m=m: v(r,p)%m
    feats['min(v%d,3)'%p]=lambda x,r,p=p: min(v(r,p),3)
for m in [2,3,4]:
    feats['Omega mod %d'%m]=lambda x,r,m=m: sum(r.values())%m
    feats['omega mod %d'%m]=lambda x,r,m=m: len(r)%m
feats['support<=13']=lambda x,r: tuple(p in r for p in [2,3,5,7,11,13])
feats['odd part squarefree']=lambda x,r: all(e==1 for p,e in r.items() if p>2)
feats['sigma odd (sq or 2sq)']=lambda x,r: all(e%2==0 for p,e in r.items() if p>2)
feats['v2+1 Mersenne exp']=lambda x,r: (v(r,2)+1) in MEXP
feats['big Mersenne divides']=lambda x,r: tuple(r.get(2**p-1,0)>0 for p in [13,17,19,31,61,89])
feats['(v2 mod2,v3 mod2)']=lambda x,r: (v(r,2)%2,v(r,3)%2)
feats['(x mod 3,v2 mod 2)']=lambda x,r: (x%3,v(r,2)%2)
feats['#primes>1000']=lambda x,r: min(sum(1 for p in r if p>1000),3)
feats['parity of exps>1 (odd p)']=lambda x,r: tuple(sorted(e%2 for p,e in r.items() if p>2 and e>1))[:3]
res=[]
for name,f in feats.items():
    val={x:f(x,F[x]) for x in F}
    if len(set(val.values()))<2: continue
    trans=defaultdict(Counter)
    for x in X: trans[val[x]][val[nxt[x]]]+=1
    det=sum(c.most_common(1)[0][1] for c in trans.values())/len(X)
    const=sum(1 for x in X if val[x]==val[nxt[x]])/len(X)
    # baseline determinism if next value independent of current
    marg=Counter(val[nxt[x]] for x in X); base=marg.most_common(1)[0][1]/len(X)
    res.append((det-base,name,det,base,const))
res.sort(reverse=True)
print('%-28s %6s %6s %6s %6s'%('feature','det','base','gain','const'))
for g,name,det,base,const in res: print('%-28s %.3f  %.3f  %+.3f  %.3f'%(name,det,base,g,const))
