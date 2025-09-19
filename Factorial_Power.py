# Factorial_Power.py


# https://open.kattis.com/problems/factorialpower
from math import floor,sqrt

def legendre(m,n):
    s = 0
    n_pow = n
    div = floor(m/n_pow)
    while div!=0:
        s += div
        n_pow *= n
        div = floor(m/n_pow)
    return s

def prime_factors(n):
    factors = []
    for i in range(int(sqrt(n))):
        if n%i==0:
            factors.append(i)

def legendre_table(n,factors):
    lg_dict = dict()
    for factor in factors:
        lg_dict[factor] = legendre(n,factor)
    return lg_dict

n,m = map(int,input().split())
print(legendre(m,n))
