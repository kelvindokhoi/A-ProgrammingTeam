# Rock_Scissors_Paper.py

# rockscissorspaper
# https://open.kattis.com/problems/rockscissorspaper

# python Rock_Scissors_Paper.py < Rock_Scissors_Paper_in.txt

beaten = {'R':'P','P':'S','S':'R'}
def update(board:list,row:int,collumn:int):
    newboard = [['' for _ in range(collumn)] for _ in range(row)]
    for i in range(row):
        for j in range(collumn):
            changes = False
            beaten_by = beaten[board[i][j]]
            if 0<=i+1<row and beaten_by == board[i+1][j]:changes = True
            if 0<=i-1<row and beaten_by == board[i-1][j]:changes = True
            if 0<=j+1<collumn and beaten_by == board[i][j+1]:changes = True
            if 0<=j-1<collumn and beaten_by == board[i][j-1]:changes = True
            newboard[i][j] = beaten_by if changes else board[i][j]
    return newboard

C = int(input())
for x in range(C):
    row,collumn,day = map(int,input().split())
    board = [list(input())for _ in[0]*row]
    for _ in[0]*day:
        board = update(board,row,collumn)
    for line in board:
        print(''.join(line))
    if x!=C-1:
        print()

# golfed:
# b={'R':'P','P':'S','S':'R'}
# def u(B,r,c,n):
#  for i in range(r):
#   for j in range(c):
#    v=b[B[i][j]];n[i][j]=v if(i and B[i-1][j]==v)or(i+1<r and B[i+1][j]==v)or(j and B[i][j-1]==v)or(j+1<c and B[i][j+1]==v)else B[i][j]
#  return n
# for x in range(int(input())):
#  r,c,d=map(int,input().split());A=[list(input())for _ in[0]*r];[A:=u(A,r,c,[a[:]for a in A])for _ in[0]*d];[print(*a,sep='')for a in A]
#  if x:print()