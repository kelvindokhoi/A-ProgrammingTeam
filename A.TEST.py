n=46340
k=[1]*n
for i in range(2,215):
    if k[i]: k[i*i:n:i]=[0]*-(-n//i+i)
P=[i for i in range(2,n) if k[i]]
def L(n,f,s=0,c=1):
    while n>=(c:=c*f): s+=n//c
    return s
for l in open(0):
    a,b=map(int,l.split())
    result=b>=1
    if result:
        for p in P:
            if p*p>b: break
            if b%p<1:
                c=0
                while b%p<1: c+=1; b//=p
                if c>L(a,p): result=False; break
        if result and not (b<2 or b<=a and 0<L(a,b)): result=False
    print(b,'divides'if result else'does not divide',f'{a}!')