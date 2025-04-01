# Beads
def kmp(t,p):
    n,m=len(t),len(p);l=[0]*m;j=0
    if m<1:return[0]*(n>-1)
    if n<1:return[]
    for i in range(1,m):
        while j and p[i]!=p[j]:j=l[j-1]
        j+=p[i]==p[j];l[i]=j
    i=j=0;r=[]
    while i<n:
        while i<n and j<m and t[i]==p[j]:i,j=i+1,j+1
        if j==m:r+=[i-j];j=l[j-1]
        elif j:j=l[j-1]
        else:i+=1
    return r

for _ in range(1,int(input())+1):
    b1 = input()
    b2 = input()*2
    print(f"Case #{_}: {'YES'if kmp(b2,b1)!=[] or kmp(b2,b1[::-1])!=[] else 'NO'}")
