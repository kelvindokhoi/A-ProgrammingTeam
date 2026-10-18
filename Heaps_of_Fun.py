# Heaps of Fun
# https://open.kattis.com/problems/heapsoffun
from fractions import Fraction
MOD = 10**9+7
n = int(input())
heap = [list(map(int,input().split())) for _ in range(n)]
heap.sort(key=lambda x:x[1])
prob = [Fraction(1,1) for _ in range(n)]

# from random import randint
def p_equal(n):
    return n*(n-1)//2
def prob_child_lt_parent(parent,child):
    child+=1
    parent+=1
    if child<=parent:
        # print(f"{(parent-child)=}, {p_equal(child)=}")
        return Fraction(((parent-child)*child+p_equal(child)),((parent)*(child)))
    else:
        return Fraction((p_equal(parent)),(parent*child))

for i in range(n-1,0,-1):
    parent = (i-1)//2
    prob[i] = prob_child_lt_parent(heap[parent][0],heap[i][0])
    # print(f"{i=}, {prob[i]=}")

p = q = 1
for r in prob:
    p *= r.numerator
    q *= r.denominator
print(prob)
print((p*pow(q,-1,MOD))%MOD)