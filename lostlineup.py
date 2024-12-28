# lostlineup

r=[1]+[0]*~-int(input())
for i,x in enumerate(map(int,input().split())):r[x+1]=i+2
print(*r)