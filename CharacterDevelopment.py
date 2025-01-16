from math import factorial


n=int(input())

def ssum(n):
    k=0
    if n==0 or n==1:
        return 0
    for i in range(2,n):
        k+= factorial(n)/factorial(n-i)/factorial(i)
    return k+1

print(int(ssum(n)))