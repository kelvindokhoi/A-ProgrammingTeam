# Sums of Primes
#Sieve of Eratosthenes

from math import*;r,z=range,int
def p(n):
 k=[1]*(n-2)
 for i in r(2,z(sqrt(n))+1):
  if k[i-2]==1:
   j=i*i
   while j<n:
    k[j-2]=0;j+=i
 return sum([i+2 for i in r(n-2)if k[i]==1])
print(p(z(input())))


