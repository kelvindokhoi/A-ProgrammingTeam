# Turtle_Master.py

# turtlemaster
# https://open.kattis.com/problems/turtlemaster

# python Turtle_Master.py < Turtle_Master_in.txt

def No_Error(board:list,turtle_x:int,turtle_y:int,move:str):
    if move=='F':
        turtle_dir = board[turtle_y][turtle_x]
        if turtle_dir=='^':
            turtle_y -= 1
        if turtle_dir=='>':
            turtle_x += 1
        if turtle_dir=='<':
            turtle_x -= 1
        if turtle_dir=='↓':
            turtle_y += 1
        if not (7>=turtle_y>=0 and 7>=turtle_x>=0):
            return False
        return board[turtle_y][turtle_x] in ['.','D']
    if move=='L' or move=='R':
        return True
    if move=='X':
        turtle_dir = board[turtle_y][turtle_x]
        if turtle_dir=='^':
            turtle_y -= 1
        if turtle_dir=='>':
            turtle_x += 1
        if turtle_dir=='<':
            turtle_x -= 1
        if turtle_dir=='↓':
            turtle_y += 1
        if not (7>=turtle_y>=0 and 7>=turtle_x>=0):
            return False
        return board[turtle_y][turtle_x]=='I'
    return False

board = [list(input())for _ in[0]*8]
Diamond_Loc = None
for j in range(8):
    for i in range(8):
        if board[j][i]=='D':
            Diamond_Loc = (i,j)
            break
command = input()
turtle_x = 0
turtle_y = 7
board[7][0] = '>'
for move in command:
    if not No_Error(board,turtle_x,turtle_y,move):
        print('Bug!')
        # print(move)
        # print(*board,sep='\n')
        exit()
    if move=='F':
        turtle_dir = board[turtle_y][turtle_x]
        board[turtle_y][turtle_x] = '.'
        if turtle_dir=='^':
            turtle_y -= 1
        if turtle_dir=='>':
            turtle_x += 1
        if turtle_dir=='<':
            turtle_x -= 1
        if turtle_dir=='↓':
            turtle_y += 1
        board[turtle_y][turtle_x] = turtle_dir
    elif move=='L':
        turtle_dir = board[turtle_y][turtle_x]
        board[turtle_y][turtle_x] = {'^':'<','<':'↓','↓':'>','>':'^'}[turtle_dir]
    elif move=='R':
        turtle_dir = board[turtle_y][turtle_x]
        board[turtle_y][turtle_x] = {'^':'>','>':'↓','↓':'<','<':'^'}[turtle_dir]
    elif move=='X':
        turtle_dir = board[turtle_y][turtle_x]
        if turtle_dir=='^':
            board[turtle_y-1][turtle_x] = '.'
        if turtle_dir=='>':
            board[turtle_y][turtle_x+1] = '.'
        if turtle_dir=='<':
            board[turtle_y][turtle_x-1] = '.'
        if turtle_dir=='↓':
            board[turtle_y+1][turtle_x] = '.'
    else:
        print('Bug!')
        exit()
if Diamond_Loc is None:
    print('Bug!')
    exit()
print('Diamond!'if (turtle_x,turtle_y) == Diamond_Loc else 'Bug!')