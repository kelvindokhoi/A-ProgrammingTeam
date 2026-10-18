# Unlock Pattern
# https://open.kattis.com/contests/jesw36/problems/unlockpattern
from math import dist
passcode = dict()
for i in range(3):
    for j,num in enumerate(map(int,input().split())):
        passcode[num]=(i,j)
sum_dst = 0
for i in range(1,9):
    sum_dst += dist(passcode[i],passcode[i+1])
print(sum_dst)