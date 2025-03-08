# Crop Triangles (Easy)
def trian(a,b,c):
    m=(a[0]+b[0]+c[0])/3
    n=(a[1]+b[1]+c[1])/3
    if m.is_integer() and n.is_integer():
        return True
    else:
        return False

testcases = int(input())
for i in range(1,testcases+1):
    ans=0
    n,A,B,C,D,x0,y0,M = map(int,input().split())
    # print trees
    alltrees = [[]for _ in range(n)]
    X=x0
    Y=y0
    alltrees[0]=(X,Y)
    for w in range(1,n-1):
        X=(A*X+B)%M
        Y=(C*Y+D)%M
        alltrees[w]=(X,Y)
    for o in range(n):
        for p in range(o+1,n):
            for l in range(p+1,n):
                if trian(alltrees[o],alltrees[p],alltrees[l]):
                    ans+=1
    print(f"Case #{i}: {ans}")

