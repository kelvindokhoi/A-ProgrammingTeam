# bunnytownbonding.py

# python bunnytownbonding.py
from statistics import median
inp = input()
bunnies = [a for (a,b) in enumerate(inp) if b=='B']
normalized = [a-b for a,b in enumerate(bunnies)]
med = median(normalized)
print(int(sum(abs(x-med) for x in normalized)))

from statistics import*;e=enumerate
N=[a-b for a,b in e(a for a,b in e(input())if b=='B')]
print(int(sum(abs(x-median(N)) for x in N)))

    