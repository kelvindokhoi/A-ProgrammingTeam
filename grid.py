# grid


# BFS worked

from collections import deque
myQ = deque()
myQ.append([0,0,0])
bx, by = map(int,input().split())
board = [input() for _ in range(bx)]
traveled = [[0 for _ in range(by)] for _ in range(bx)]
def inbound(px,py):
    return -1<px<bx and -1<py<by
while myQ:
    px,py,steps_taken = myQ.popleft()
    if px==bx-1 and py==by-1:
        print(steps_taken)
        exit()
    if traveled[px][py]:
        continue
    traveled[px][py] = 1
    value = int(board[px][py])
    if inbound(px+value,py):
        myQ.append([px+value,py,steps_taken+1])
    if inbound(px,py+value):
        myQ.append([px,py+value,steps_taken+1])
    if inbound(px-value,py):
        myQ.append([px-value,py,steps_taken+1])
    if inbound(px,py-value):
        myQ.append([px,py-value,steps_taken+1])
print(-1)



# This backtracking got TLE-ed 


# move = [float('inf')]
# bx, by = map(int,input().split())
# board = [input() for _ in range(bx)]
# traveled = [[0 for _ in range(by)] for _ in range(bx)]

# def debug_wrapper(func):
#     def wrapper(*args):
#         print(f"Entering {func.__name__} with args: {args}")
#         result = func(*args)
#         print(f"Exiting {func.__name__} with result: {result}")
#         return result
#     return wrapper

# # @debug_wrapper
# def Backtracking(board,traveled,bx,by,px,py,move,steps_taken):
#     if px==bx-1 and py==by-1:
#         move[0] = min(move[0],steps_taken)
#         return
#     if not (0<=px<bx) or not (0<=py<by) or traveled[px][py]:
#         return
#     traveled[px][py] = 1
#     value = int(board[px][py])
#     if 0<=px+value<bx:
#         Backtracking(board,traveled,bx,by,px+value,py,move,steps_taken+1)
#     if 0<=py+value<by:
#         Backtracking(board,traveled,bx,by,px,py+value,move,steps_taken+1)
#     if 0<=px-value<bx:
#         Backtracking(board,traveled,bx,by,px-value,py,move,steps_taken+1)
#     if 0<=py-value<by:
#         Backtracking(board,traveled,bx,by,px,py-value,move,steps_taken+1)
#     traveled[px][py] = 0

# Backtracking(board,traveled,bx,by,0,0,move,0)
# if move[0]!=float('inf'):
#     print(move[0])
# else:
#     print(-1)    

