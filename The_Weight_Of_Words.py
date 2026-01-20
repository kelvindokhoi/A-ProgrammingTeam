# The Weight Of Words
# https://open.kattis.com/contests/iyszhk/problems/weightofwords

length, weight = map(int,input().strip().split())

def checklegit(charmap):
    for char in charmap:
        if char==0 or char>26:
            return True
    return False
charmap = [0 for _ in ' '*length]

for i in range(weight):
    charmap[i%length] += 1

if checklegit(charmap):
    print("impossible")
else:
    print(''.join(chr(ord('a')+x-1) for x in charmap))