from math import dist
from collections import deque
# Kruskal
# DFS
# DP


class Union_Find():
    def __init__(self,n):
        self.parents = [*range(n)]
        self.rank = [0]*n
    def find(self,x):
        if self.parents[x]!=x:
            self.parents[x]=self.find(self.parents[x])
        return self.parents[x]
    def union(self,x,y):
        dx,dy=self.find(x),self.find(y)
        if dx==dy:
            return False
        if self.rank[dx]>self.rank[dy]:
            self.parents[dy] = dx
        elif self.rank[dx]<self.rank[dy]:
            self.parents[dx] = dy
        else:
            self.parents[dx]=dy
            self.rank[dy]+=1
        return True

counter = 1
while True:
    n=int(input())
    if n==0:break
    points = [[*map(int,input().split())]for _ in range(n)]
    input()
    edges = []
    for i in range(n):
        for j in range(i+1,n):
            edges.append((dist(points[i],points[j]),i,j))
    edges.sort()
    uf = Union_Find(n)
    MST_edges = []
    for edge in edges:
        d,x,y = edge
        if uf.union(x,y):
            MST_edges.append(edge)
            if len(MST_edges)==n-1:
                break
    MST_adjacency_list = [[]for _ in range(n)]
    for d,x,y in MST_edges:
        MST_adjacency_list[x].append((d,y))
        MST_adjacency_list[y].append((d,x))
    maxjump = [-1]*n
    maxjump[0] = 0
    myq = deque([0])
    while myq:
        curr = myq.popleft()
        for d,p in MST_adjacency_list[curr]:
            if maxjump[p]==-1:
                maxjump[p] = max(maxjump[curr],d)
                myq.append(p)
    print(f"Scenario #{counter}")
    counter+=1
    print(f"Frog Distance = {maxjump[1]:.3f}")
    print()



