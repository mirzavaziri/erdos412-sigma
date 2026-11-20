import random, math, sys
def ip(n):
    if n<2: return False
    for p in [2,3,5,7,11,13,17,19,23,29,31,37]:
        if n%p==0: return n==p
    d,s=n-1,0
    while d%2==0: d//=2;s+=1
    for a in [2,3,5,7,11,13,17,19,23,29,31,37]:
        x=pow(a,d,n)
        if x in(1,n-1): continue
        for _ in range(s-1):
            x=x*x%n
            if x==n-1: break
        else: return False
    return True
def rho(n):
    if n%2==0: return 2
    while True:
        c=random.randrange(1,n);f=lambda x:(x*x+c)%n
        x=y=random.randrange(2,n);d=1
        while d==1: x=f(x);y=f(f(y));d=math.gcd(abs(x-y),n)
        if d!=n: return d
def fac(n,r):
    if n==1: return
    for p in range(2,2000):
        while n%p==0: r[p]=r.get(p,0)+1; n//=p
    st=[n] if n>1 else []
    while st:
        m=st.pop()
        if ip(m): r[m]=r.get(m,0)+1
        else: d=rho(m); st+= [d,m//d]
def sig(n):
    r={};fac(n,r);s=1
    for p,e in r.items(): s*=(p**(e+1)-1)//(p-1)
    return s
if __name__=="__main__":
    B=10**int(sys.argv[2]); N=int(sys.argv[1])
    par=list(range(N+1))
    def f(x):
        while par[x]!=x: par[x]=par[par[x]]; x=par[x]
        return x
    seen={}
    for n in range(2,N+1):
        x=n
        while x<B:
            if x in seen: par[f(n)]=f(seen[x]); break
            seen[x]=n; x=sig(x)
    cl={}
    for n in range(2,N+1): cl.setdefault(f(n),[]).append(n)
    print(len(cl)); 
    for k,v in sorted(cl.items(),key=lambda t:-len(t[1]))[:8]: print(len(v),v[:12])
    