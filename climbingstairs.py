# climbingstairs
from math import ceil

c,a,b=map(int,input().split())
ans=[2*a+2*b*ceil((c-2*a)/(2*b)),2*b+2*a*ceil((c-2*b)/(2*a))]
if c-2*(a+b)>0:
    print(min(ans))
else:
    print(2*(a+b))