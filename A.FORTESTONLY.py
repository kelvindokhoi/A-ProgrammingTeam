h,w,n,*b=map(int,open(0).read().split());q,r,z=[0]*h,0,1
for k in b:
 if r<h:q[r]+=k;z&=q[r]<=w;r+=q[r]==w
print(['NO','YES'][(q[-1]==w)*z])
