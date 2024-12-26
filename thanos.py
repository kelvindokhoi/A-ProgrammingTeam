# thanos


from math import log,ceil

def fast(b,p):
    res=1
    while p:
        if p&1:res*=b
        b*=b
        p>>=1
    return res

t = int(input())
for _ in range(t):
    p, r, f = map(int, input().split())
    if p > f:
        print(0)
    else:
        years = ceil(log(f/p, r))
        if p*fast(r,years)-f:
            print(years)
        else:  
            print(years+1)


# from math import log,ceil
# x=lambda b,p:b if p==1 else b*x(b*b,p//2)if p&1 else x(b*b,p//2);t=int(input())
# for _ in[0]*t:p,r,f=map(int,input().split());y=ceil(log(f/p,r))if p<f else 0;print(y+int(p*x(r,y)<=f))