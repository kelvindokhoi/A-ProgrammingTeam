# tictactoesolver.py
# https://open.kattis.com/problems/tictactoesolver

board = [list(input()) for _ in range(3)]

def check_diag(symbol,li):
    return li[0][0]==li[1][1]==li[2][2]==symbol or li[2][0]==li[1][1]==li[0][2]==symbol
def check_hori(symbol,li):
    for i in range(3):
        if li[i][0]==li[i][1]==li[i][2]==symbol:
            return True
    return False
def check_verti(symbol,li):
    for i in range(3):
        if li[0][i]==li[1][i]==li[2][i]==symbol:
            return True
    return False
def check_win(symbol,li):
    return check_diag(symbol,li) or check_hori(symbol,li) or check_verti(symbol,li)

if check_win("X",board):
    print("X")
elif check_win("O",board):
    print("O")
else:
    print("N")