# trilemma
# Triangle Trilemma
# https://open.kattis.com/problems/trilemma
from math import acos, dist

def checklength(p1,p2,p3):
    side1 = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    side2 = (p2[0]-p3[0])**2 + (p2[1]-p3[1])**2
    side3 = (p1[0]-p3[0])**2 + (p1[1]-p3[1])**2
    if side1==side2 or side2==side3 or side1==side3:
        return 'isosceles'
    return "scalene"
def dot_prod(p1,p2):
    return p1[0]*p2[0]+p1[1]*p2[1]
def vec(p1,p2):
    return (p1[0]-p2[0],p1[1]-p2[1])
def vec_length(p1):
    return dist(p1,(0,0))

def angle_2vec(v1,v2):
    return acos(dot_prod(v1,v2)/(vec_length(v1)*vec_length(v2)))

def angle_check(p1, p2, p3):
    dots = (
        dot_prod(vec(p2, p1), vec(p3, p1)),
        dot_prod(vec(p1, p2), vec(p3, p2)),
        dot_prod(vec(p1, p3), vec(p2, p3)),
    )
    if 0 in dots:
        return "right"
    if any(d < 0 for d in dots):
        return "obtuse"
    return "acute"

def straight_line(p1,p2,p3):
    return (p1[0]-p2[0])*(p1[1]-p3[1]) == (p1[1]-p2[1])*(p1[0]-p3[0])
def check_if_triangle(p1,p2,p3):
    if p1==p2 or p2==p3 or p1==p3:
        return False
    if straight_line(p1,p2,p3):
        return False
    return True

n = int(input())
for i in range(1,n+1):
    x1,y1,x2,y2,x3,y3 = map(int,input().split())
    p1,p2,p3 = (x1,y1),(x2,y2),(x3,y3)
    if check_if_triangle(p1,p2,p3):
        print(f"Case #{i}: {checklength(p1,p2,p3)+' '}{angle_check(p1,p2,p3)+' '}triangle")
    else:
        print(f"Case #{i}: not a triangle")
