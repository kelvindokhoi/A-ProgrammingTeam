# Single source shortest path, non-negative weights

import heapq
from math import inf

while 1:
    n,m,q,s = map(int,input().split())
    if n==m==q==s==0:
        break
    graph = {k:[] for k in range(n)}
    weightmap = {k:inf for k in range(n)}
    weightmap[s] = 0
    visited = [True]*n
    myHeap = []
    heapq.heappush(myHeap,(0,s))
    for _ in' '*m:
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
    while myHeap:
        d,u = heapq.heappop(myHeap)
        if visited[u]:
            visited[u] = False
            for v,w in graph[u]:
                if(new:=w+d)< weightmap[v]:
                    weightmap[v] = new
                    heapq.heappush(myHeap,(new,v))
    for _ in range(q):
        a = weightmap[int(input())]
        print(a if a!=inf else 'Impossible')
