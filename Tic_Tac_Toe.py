# Tic_Tac_Toe.py
# tictactoe2
# python Tic_Tac_Toe.py < Tic_Tac_Toe_in.txt
# https://open.kattis.com/problems/tictactoe2

def check_winner(board: list):
    end_pos = [(0,3,6), (0,1,2), (3,4,5), (6,7,8), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    x_wins = False
    o_wins = False
    for pos in end_pos:
        if all(board[p] == 'X' for p in pos):
            x_wins = True
        if all(board[p] == 'O' for p in pos):
            o_wins = True
    return x_wins, o_wins

def is_valid_board():
    board = input().rstrip() + input().rstrip() + input().rstrip()
    x_count = board.count('X')
    o_count = board.count('O')
    
    # Check move counts
    if o_count > x_count or x_count > o_count + 1:
        return 'no'
    
    x_wins, o_wins = check_winner(list(board))
    
    # Check for invalid dual winners
    if x_wins and o_wins:
        return 'no'
    
    # Check winning conditions
    if x_wins:
        if x_count != o_count + 1:
            return 'no'
        return 'yes'
    if o_wins:
        if x_count != o_count:
            return 'no'
        return 'yes'
    
    # For non-winning boards, check if reachable
    # Valid if move counts are correct and no invalid wins
    return 'yes'

T = int(input())
for n in range(T):
    print(is_valid_board())
    if n < T - 1:
        input()


# golfed:
# def C(b):
#  X=O=0
#  for a,b_,c in[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]:
#   if b[a]==b[b_]==b[c]!='.':X|=b[a]=='X';O|=b[a]=='O'
#  return X,O
# T=int(input())
# for n in range(T):
#  b=''.join(input().strip()for _ in[0]*3)
#  x,o=b.count('X'),b.count('O')
#  if o>x or x>o+1:print('no')
#  else:
#   X,O=C(b)
#   print('no'if X&O or(X and x!=o+1)or(O and x!=o)else'yes')
#  if n<T-1:input()