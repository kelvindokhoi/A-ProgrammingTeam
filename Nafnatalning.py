# Nafnatalning
# https://open.kattis.com/problems/nafnatalning

from math import ceil
n,P = map(int,input().split())
ith = list(map(int,input().split()))

total_pairs = 0
s = sum(ith)
for i in range(n):
    total_pairs += ith[i]*(s-ith[i])

print(ceil(total_pairs/2/P))