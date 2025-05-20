# Where's My Internet??

# python Wheres_My_Internet.py

from collections import deque

N,M = map(int,input().split())
visited = [False for _ in range(N)]
graph = {i:set() for i in range(1,N+1)}
myQ = deque()
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].add(y)
    graph[y].add(x)
myQ.append(1)
while myQ:
    v = myQ.pop()
    visited[v-1] = True
    for neighbor in graph[v]:
        if not visited[neighbor-1]:
            myQ.append(neighbor)
ans = []
for i in range(N):
    if not visited[i]:
        ans.append(i+1)
if ans:
    print(*sorted(ans),sep='\n')
else:
    print("Connected")
