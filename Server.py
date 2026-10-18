# Server
# https://open.kattis.com/problems/server

from bisect import bisect_left
n,T = map(int,input().split())

*orders, = map(int,input().split())
lim = [orders[0]]+[0]*(n-1)
for i in range(1,n):
    lim[i]=lim[i-1]+orders[i]
res =  bisect_left(lim,T)
if res==n:
    print(res)
else:
    print(res if lim[res]!=T else res+1)
