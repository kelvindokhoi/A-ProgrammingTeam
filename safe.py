# Cracking The Safe
from collections import deque







a=[[*map(int,input().split())]for i in[0]*3]
a=sum([sum(b) for b in a])
# print(a)
# print(a//3,a%3)
if a%3==0:
    print(-1)
else:
    print(a//3-a%3)
