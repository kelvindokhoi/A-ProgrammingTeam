from math import *
import heapq
for i in range(int(input())):
    input()
    untrvl = [tuple(map(float,input().split())) for _ in range(int(input()))]
    passed = set([untrvl.pop()])
    sum=0
    edges=[]
    for p1 in untrvl:
        for p2 in passed:
            heapq.heappush(edges,(dist(p1,p2),p1))
    while untrvl:
        w,point = heapq.heappop(edges)
        if point in passed:continue
        sum+=w;passed.add(point);untrvl.remove(point)
        for pt in untrvl:
            pt in passed or heapq.heappush(edges, (dist(point,pt), pt))
    print(f"{sum:.2f}")