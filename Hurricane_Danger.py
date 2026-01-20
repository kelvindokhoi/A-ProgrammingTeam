# Hurricane Danger!
# https://open.kattis.com/contests/oaojv8/problems/hurricanedanger

from math import sqrt

def distance_point_ot_plane(x1,y1,x2,y2,x3,y3):
    return abs((x2-x1)*(y3-y1)-(y2-y1)*(x3-x1))/sqrt((x2-x1)**2+(y2-y1)**2)


for i in range(int(input())):
    max_dist = float('inf')
    x1,y1,x2,y2 = map(int,input().split())
    cities = []
    for j in range(int(input())):
        name,x3,y3 = input().split()
        distance = distance_point_ot_plane(x1,y1,x2,y2,int(x3),int(y3))
        # print(distance)
        if distance < max_dist:
            max_dist = distance
            cities = [name]
        elif distance == max_dist:
            cities.append(name)
    print(" ".join(cities))

