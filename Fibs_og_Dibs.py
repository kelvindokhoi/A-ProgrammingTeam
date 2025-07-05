# Fibs_og_Dibs.py


# Fibs og Dibs
# https://open.kattis.com/problems/fibsogdibs


memo = {0:0,1:1,2:1}
from math import sqrt

def fib(n):
    if n in memo:
        return memo[n]
    # if n<=71:
    #     memo[n] = int(1/sqrt(5)*(((1+sqrt(5))/2)**n-((1-sqrt(5))/2)**n))%m
    #     return memo[n]
    k = n//2
    if n%2==0:
        memo[n]=fib(k)*(2*fib(k+1)-fib(k))%m
        return memo[n]
    else:
        memo[n]=(fib(k+1)**2 + fib(k)**2)%m
        return memo[n]

a,b = map(int,input().split())
n = int(input())
m = 10**9+7
a,b = a%m,b%m
if n!=0:
    f0 = fib(2*n-1)%m
    f1 = fib(2*n)%m
    f2 = (f0+f1)%m
    print((a*f0+b*f1)%m,(a*f1+b*f2)%m)
else:
    print(a,b)