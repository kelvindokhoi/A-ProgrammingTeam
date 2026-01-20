# Name That Permutation
# https://open.kattis.com/contests/iyszhk/problems/namethatpermutation

# python Name_That_Permutation.py < Name_That_Permutation_in.txt

from math import factorial

for line in open(0).read().splitlines():
    n,k = map(int,line.strip().split())
    switcher = [1 for _ in ' '*n]
    choices = list(range(1,n+1))
    result = []
    for i in range(n-1):
        f_i = factorial(n-i-1)
        cycles = k//f_i
        k -= cycles*f_i
        result.append( choices.pop(cycles))
    result.append(choices[0])
    print(' '.join(str(x) for x in result))