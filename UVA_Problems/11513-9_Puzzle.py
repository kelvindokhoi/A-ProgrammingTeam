# 11513-9_Puzzle.py

from collections import deque
def move(original, type, val):
    new = list(original)
    if type == 1:  # case h, which is -> right
        row_start = (val - 1) * 3
        new[row_start], new[row_start + 1], new[row_start + 2] = new[row_start + 1], new[row_start+2], new[row_start]
    else:  # case v, which is -> up
        col_start = val - 1
        new[col_start], new[col_start + 3], new[col_start + 6] = new[col_start + 6], new[col_start], new[col_start + 3]
    return ''.join(new)

cached_Solution = {'123456789':('',0)}
mydeq = deque()
mydeq.append(['123456789','',0])
while mydeq:
    current,sol,num_mov = mydeq.popleft()
    num_mov+=1
    for i in range(1, 4):
        H = move(current, 1, i)
        if H not in cached_Solution:
            cached_Solution[H] = (f'H{i}'+sol, num_mov)
            mydeq.append((H, f'H{i}'+sol, num_mov))
        V = move(current, 0, i)
        if V not in cached_Solution:
            cached_Solution[V] = (f'V{i}'+sol, num_mov)
            mydeq.append((V, f'V{i}'+sol, num_mov))
# print(cached_Solution) #the fcking sols
n1=input().split()
while True:
    if n1==['0']:
        break
    n2=input().split()
    n3=input().split()
    grid=n1+n2+n3
    grid=''.join(grid)
    if grid in cached_Solution:
        solution,num = cached_Solution[grid]
        print(num,solution)
    else:
        print('Not solvable')
    n1=input().split()
