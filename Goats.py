# Goats
from math import sqrt, acos, pi


def calc_middle(a,b,c,a2,b2,c2):return a2*acos((c2-b2+a2)/(2*c*a)) + b2*acos((c2-a2+b2)/(2*b*c)) - sqrt((c-a+b)*(c+a-b)*(a+b-c)*(c+a+b))/2

def BinarySearch(tries,min_a,max_a,b,c):
    a = (min_a+max_a)/2
    a2 = a**2
    b2 = b**2
    c2 = c**2
    lhs = pi*b2
    for _ in' '*tries:
        # too far no intersect
        if c>=a+b:
            rhs = pi*a2
        # c2 inside c1
        elif a-b>=c and a>=b:
            rhs = pi*(a2-b2)
        # c1 inside c2
        elif b>=a+c and b>=a:
            rhs = 0
        else:
            rhs = pi*a2-calc_middle(a,b,c,a2,b2,c2)
        if abs(rhs-lhs)<1e-9:
            return a
        if rhs>lhs:
            max_a = a
        else:
            min_a = a
        a = (max_a+min_a)/2
        a2 = a**2
    return a

for _ in' '*int(input()):
    b,c = map(float,input().split())
    a = BinarySearch(10000,0,2e9,b,c)
    result = pi*a*a - (calc_middle(a,b,c,a*a,b*b,c*c) if c<a+b and abs(a-b)<c else (pi*b*b if a>=b and a-b>=c else 0))
    print(f'{result} = {pi*b*b}, with a = {a}')
