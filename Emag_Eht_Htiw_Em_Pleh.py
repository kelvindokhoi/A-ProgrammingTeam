# Emag Eht Htiw Em Pleh
# empleh

board = [[]for _ in range(8)]
# for i in range(0,17,2):
#     board[i]= [*'+---+---+---+---+---+---+---+---+']
for i in range(0,8):
    if i % 2 ==0:
        board[i]= [*'|...|:::|...|:::|...|:::|...|:::|']
    else:
        board[i]= [*'|:::|...|:::|...|:::|...|:::|...|']
white = input()[7:].split(sep=',')
black = input()[7:].split(sep=',')
for piece in white:
    if len(piece)==0:
        break
    if len(piece)==3:
        name,col,row = piece
    else:
        name,col,row = 'p'+piece
    board[8-int(row)][2+4*(ord(col)-ord('a'))] = name.upper()
for piece in black:
    if len(piece)==0:
        break
    if len(piece)==3:
        name,col,row = piece
    else:
        name,col,row = 'P'+piece
    board[8-int(row)][2+4*(ord(col)-ord('a'))] = name.lower()
for row in board:
    print('+---+---+---+---+---+---+---+---+')
    print(''.join(row))
print('+---+---+---+---+---+---+---+---+')