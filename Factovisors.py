# Factovisors

# python Factovisors.py < Factovisors_in.txt
#Sieve of Eratosthenes
from math import sqrt
from bisect import bisect_right

def prime(n):
    k=[True]*(n-2)
    for i in range(2,int(sqrt(n))+1):
        if k[i-2]==True:
            j=i*i
            while j<n:
                k[j-2]=False
                j+=i
    return [i+2 for i in range(n-2) if k[i]==True]
list_of_all_prime = prime(46340) #cuz m,n can get to 2^31

# Legendre's Formular (for finding the number of k factor)
def legendre(num,factor):
    s=0
    curr = factor
    while num>=curr:
        s+=num//curr
        curr*=factor
    return s

def check_divisible(a,b):
    if a==0:
        return b==1
    if b==0:
        return False
    limit = bisect_right(list_of_all_prime,a)
    factorized = {}
    for factor in list_of_all_prime[:limit]:
        factorized[factor]=legendre(a,factor)
    # print(f"Factorized: {factorized}")
    limit_b = bisect_right(list_of_all_prime,(b**0.5)//1+1)
    for factor_b in list_of_all_prime[:limit_b]:
        if b==1:break
        if b%factor_b==0:
            count = 1
            b = b//factor_b
            while b%factor_b==0:
                count+=1
                b = b//factor_b
            if factor_b not in factorized or count>factorized[factor_b]:
                # print(f'Failed at: {factor_b}, count {count}')
                return False
    if b>a:
        return False
    else:
        if b==1:
            return True
        else:
            return b<=a

while True:
    try:
        a,b = map(int,input().split())
        # a! vs. b
        print(f'{b} divides {a}!'if check_divisible(a,b) else f'{b} does not divide {a}!')
    except EOFError:
        break