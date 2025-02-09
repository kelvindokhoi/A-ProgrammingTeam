# collatz.py
# Collatz Conjecture
import math

def Collatz(a):
    if a&1:
        return 3*a+1
    else:
        return a//2
    
while ((a:=[*map(int,input().split())])!=[0,0]):
    set1={a[0]};set2={a[1]}
    col1=[a[0]];col2=[a[1]]
    x=a[0]
    while x!=1:
        x=Collatz(x)
        col1.append(x);set1.add(x)
    col1.append(1);set1.add(1)
    y=a[1]
    while y!=1:
        y=Collatz(y)
        col2.append(y);set2.add(y)
    col2.append(1);set2.add(1)
    general= set1&set2
    meet=0
    total =math.inf
    step1=0
    step2=0
    for common in general:
        m=col1.index(common)
        n=col2.index(common)
        if m+n<total:
            total=m+n
            step1=m
            step2=n
            meet=common
    print(f"{a[0]} needs {step1} steps, {a[1]} needs {step2} steps, they meet at {meet}")
