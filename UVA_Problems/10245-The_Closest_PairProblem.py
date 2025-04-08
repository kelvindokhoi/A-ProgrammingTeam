# 10245 - The Closest Pair Problem

# python UVA_Problems/10245-The_Closest_PairProblem.py < UVA_Problems/10245-The_Closest_PairProblem_in.txt
# python 10245-The_Closest_PairProblem.py < 10245-The_Closest_PairProblem_in.txt
from math import dist

while True:
    n = int(input())
    if n==0:exit()
    coordinates = sorted([[*map(float,input().split())]for _ in' '*n])
    if n==1:print('INFINITY');continue
    d = dist(coordinates[0],coordinates[1])
    if n==2:print('INFINITY' if d>=10000 else f'{d:.4f}');continue
    for i in range(2,n):
        p = i-1
        new = coordinates[i]
        while p>=0:
            point = coordinates[p]
            if abs(new[0]-point[0])<=d:
                if abs(new[1]-point[1])<=2*d:
                    d = min(d,dist(new,point))
            else:break
            p-=1
    print('INFINITY' if d>=10000 else f'{d:.4f}')
