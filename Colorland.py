# Colorland
# colorland

from bisect import bisect_right
board_size = int(input())
positions = {i:[] for i in ['B','O','P','G','R','Y']}
for i in range(board_size):
    nchar = input()[0]
    positions[nchar].append(i)
curr_pos = -1
totalmove = 0
while True:
    if curr_pos==board_size-1:
        break
    new_pos = -1
    for i in ['B','O','P','G','R','Y']:
        if positions[i]:
            new = bisect_right(positions[i],curr_pos)
            if new<len(positions[i]):
                if positions[i][new]>new_pos:
                    new_pos = positions[i][new]
    curr_pos = new_pos
    totalmove+=1
print(totalmove)