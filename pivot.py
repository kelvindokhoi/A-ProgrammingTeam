# pivot
n,*m=map(int,open(0).read().split())
ans=0
arr_max=[0]*n;arr_min=[0]*n
arr_max[0]=m[0];arr_min[n-1]=m[n-1]
for i in range(1,n):
    arr_max[i]=max(m[i],arr_max[i-1])
for i in range(n-2,-1,-1):
    arr_min[i]=min(m[i],arr_min[i+1])
for i in range(n):
    if arr_max[i]<=arr_min[i]:
        ans+=1
print(ans)
