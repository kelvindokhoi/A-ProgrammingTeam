# 11513-9_Puzzle.py

# strat: shift the number to match the 0st=1, 4st=5, 8th=9.
from collections import deque
def move(original,type,val):
    new = original.copy()
    if type==1:#case h, which is -> right
        nv = val-1
        new[nv*3],new[nv*3+1],new[nv*3+2]=new[nv*3+1],new[nv*3+2],new[nv*3]
        return new
    else:#case v, which is -> up
        new[val-1],new[val+2],new[val+5]=new[val+2],new[val+5],new[val-1]
        return new

    

cached_Solution = {'123456789':('',0)}
mydeq = deque('123456789')
while mydeq:
    current = mydeq.pop()
    H1 = move(current,1,1)
    if H1 not in cached_Solution:
        pass
    H2 = move(current,1,2)
    H3 = move(current,1,3)
    V1 = move(current,0,1)
    V2 = move(current,0,2)
    V3 = move(current,0,3)
while (n1:=input().split())!='0':
    n2=input().split()
    n3=input().split()
    grid=n1+n2+n3
    
