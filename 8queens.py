# 8queens.py


board=[input()for _ in' '*8]

def conflict(row,col):
    for i in range(8):
        if i!=row and board[i][col] == "*":
            return True
        if i!=col and board[row][i] == "*":
            return True
    for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
        if board[i][j]=='*':
            return True
    for i,j in zip(range(row+1,8,1),range(col-1,-1,-1)):
        if board[i][j]=='*':
            return True
    for i,j in zip(range(row-1,-1,-1),range(col+1,8,1)):
        if board[i][j]=='*':
            return True
    for i,j in zip(range(row+1,8,1),range(col+1,8,1)):
        if board[i][j]=='*':
            return True


def main():
    for r in range(8):
        # Check for conflicts
        if board[r].count('*')!=1 or conflict(r,board[r].index('*')):
            print('invalid');return
    print('valid')


main()
