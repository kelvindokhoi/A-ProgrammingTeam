# artichoke
# Amalgamated Artichokes
from math import sin,cos

p,a,b,c,d,n=map(int,input().split())
prices=[p*(sin(a*k+b)+cos(c*k+d)+2) for k in range(1,n+1)]
bgap=0
highest=prices[0]
for i in range(1,n):
    if prices[i]>highest:
        highest=prices[i]
    elif highest - prices[i]>bgap:
        bgap = (highest - prices[i]) 
print(bgap)