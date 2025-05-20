# Easter Eggs

# python Easter_Eggs.py
from math import dist
from heapq import *

class Node:
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def loc(self):
        return self.x,self.y
    def __repr__(self):
        return f'{self.x} {self.y} {self.color}'
    def __gt__(self,other):
        return self.loc()>other.loc()

Eggs_2_Hide, NBlueberry, NRedberry = map(int,input().split())
Allberries = []
for i in ' '*NBlueberry:
    Allberries.append(Node(*map(int,input().split()),'B'))
for i in ' '*NRedberry:
    Allberries.append(Node(*map(int,input().split()),'R'))
travelled = {Allberries.pop()}
edges = []
solution = []
for _ in range(NBlueberry+NRedberry):
    for p1 in travelled:
        for p2 in Allberries:
            if p1.color!=p2.color:
                heappush(edges,(-dist(p1.loc(),p2.loc()),p1,p2))
    while Allberries:
        w,p1,p2 = heappop(edges)
        if p2 in travelled:
            continue
        travelled.add(p2)
        Allberries.remove(p2)
        heappush(solution,(w,p1,p2))
        for pt in Allberries:
            if pt not in travelled:
                if p2.color != pt.color:
                    heappush(edges,(-dist(p2.loc(),pt.loc()),p2,pt))
# print(solution)
minimal = float('inf')
for _ in range(Eggs_2_Hide-1):
    w, p1,p2 = heappop(solution)
    minimal = min(minimal,-w)
print(f"{minimal:.6f}")