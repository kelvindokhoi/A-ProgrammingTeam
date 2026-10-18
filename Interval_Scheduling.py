# Interval Scheduling

# python Interval_Scheduling.py < Interval_Scheduling_in.txt
from math import dist

char_d = dict()
for n,c in enumerate("qwertyuiop"):
    char_d[c] = (0,n)
for n,c in enumerate("asdfghjkl"):
    char_d[c] = (1,n)
for n,c in enumerate("zxcvbnm"):
    char_d[c] = (2,n)

def comp_char(c1,c2):
    n1,n2 = (char_d[c1],char_d[c2])
    return abs(n1[0]-n2[0])+abs(n1[1]-n2[1])

def comp_word(w1,w2):
    return sum(comp_char(a,b) for a,b in zip(w1,w2))

num_case = int(input())
for _ in range(num_case):
    allw = []
    word, repeat = input().split()
    for _ in range(int(repeat)):
        w2 = input()
        allw.append((comp_word(word,w2),w2))
    allw.sort()
    for count,w2 in allw:
        print(w2,count)