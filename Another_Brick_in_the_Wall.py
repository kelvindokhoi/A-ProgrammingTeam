# Another Brick in the Wall
# anotherbrick


h,w,n = map(int,input().split())
bricks = [*map(int,input().split())]
wall = [0]*h
row=0
for brick in bricks:
    if row>h-1:break
    wall[row]+=brick
    if wall[row]>w:print('NO');exit()
    if wall[row]==w:row+=1
print('YES'if wall==[w]*h else'NO')

# golfed:
# h,w,n,*b=map(int,open(0).read().split());q,r,z=[0]*h,0,1
# for k in b:
#  if r<h:q[r]+=k;q[r]<=w or(z:=0);q[r]!=w or(r:=-~r)
# print(['NO','YES'][(q[-1]==w)*z])

# ultragolfed:
# h,w,n,*b=map(int,open(0).read().split());q,r,z=[0]*h,0,1
# for k in b:
#  if r<h:q[r]+=k;z&=q[r]<=w;r+=q[r]==w
# print(['NO','YES'][(q[-1]==w)*z])
    