# Bazen
# python bazen.py
# https://open.kattis.com/contests/hgr7mz/problems/bazen

from math import sqrt

def another_point(x1,y1):
    half_pool_area = 250*125
    if x1==y1==0:
        return (125.00,125.00)
    elif x1==0 and y1==250:
        return (125.00,0.00)
    elif x1==250 and y1==0:
        return (0.00,125.00)
    elif x1==125 and y1==125:
        return 0,0
    if x1==0:
        # p1 in A
        # assume p2 in B 
        y2 = 0
        x2 = 2*half_pool_area/y1
        if x2<=250:
            return (x2,y2)
        else:
            # p2 in C 
            a = 250-y1
            b = 2*half_pool_area/(a*sqrt(2)/2)
            x2 = sqrt(2)/2*b
            y2 = 250 - x2
            return (x2,y2)
    elif y1==0:
        #p1 in B
        # assume p2 in A 
        x2 = 0
        y2 = 2*half_pool_area/x1
        if y2 <= 250:
            return (x2,y2)
        else:
            # p2 in C 
            a = 250-x1
            b = 2*half_pool_area/a*sqrt(2)
            y2 = sqrt(b*b/2)
            x2 = 250 - y2
            return (x2,y2)
    else:
        # p1 in C 
        # assume p2 in A 
        a = sqrt(x1*x1 + (250-y1)**2)
        b = 2*half_pool_area/a*sqrt(2)
        x2 = 0
        y2 = 250-b
        if y2>=0:
            return (x2,y2)
        else:
            a = sqrt((250-x1)**2+y1*y1)
            b = 2*half_pool_area/a*sqrt(2)
            x2 = 250-b
            y2 = 0
            return (x2,y2)

x1, y1 = map(int,input().split())
x2,y2 = another_point(x1,y1)
print(f"{x2:.2f} {y2:.2f}")