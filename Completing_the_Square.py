# Completing the Square
# https://open.kattis.com/contests/iyszhk/problems/completingthesquare

from math import dist

*a, = map(int,input().strip().split())
*b, = map(int,input().strip().split())
*c, = map(int,input().strip().split())

d_ab = dist(a,b)
d_bc = dist(b,c)
d_ac = dist(a,c)

if d_ab==d_ac:
    print(b[0]-a[0]+c[0],b[1]-a[1]+c[1])
elif d_ab==d_bc:
    print(a[0]-b[0]+c[0],a[1]-b[1]+c[1])
else:
    print(a[0]-c[0]+b[0],a[1]-c[1]+b[1])
