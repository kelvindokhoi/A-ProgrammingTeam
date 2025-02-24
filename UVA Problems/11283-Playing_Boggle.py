# 11283 - Playing Boggle


movements=[(0,1),(1,0),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)];scoregrid={3:1,4:1,5:2,6:3,7:5}
def solve(x,y,checked,key,grid,currid):
    if len(key)==currid:return True
    if x<0 or x>3 or y<0 or y>3 or grid[4*x+y]!=key[currid] or checked[4*x+y]:return False
    checked[4*x+y]=True
    for nx,ny in movements:
        if solve(x+nx,y+ny,checked,key,grid,currid+1):checked[4*x+y]=False;return True
    checked[4*x+y]=False
    return False
for i in range(int(input())):
    score=0;input();grid = ''.join([input().strip() for _ in range(4)])
    for j in range(int(input())):
        key=input();found=False;checked=[False]*16
        for m in range(4):
            if found:break
            for n in range(4):
                if grid[4*m+n]==key[0] and solve(m,n,checked,key,grid,0):
                    found=True;lk=len(key);score+=11 if lk>7 else scoregrid[lk];break
    print(f'Score for Boggle game #{i+1}: {score}')
    


# from time import time

# start = time()
# moves = {
#     0: ((0, 1), (1, 0), (1, 1)), 1: ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1)), 
#     2: ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1)), 3: ((0, -1), (1, 0), (1, -1)), 
#     4: ((0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)), 5: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 
#     6: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 7: ((0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1)), 
#     8: ((0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)), 9: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 
#     10: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 11: ((0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1)), 
#     12: ((0, 1), (-1, 0), (-1, 1)), 13: ((0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)), 
#     14: ((0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)), 15: ((0, -1), (-1, 0), (-1, -1))
# }
# def movevable(x, y, pastmoves):
#     return [move for move in moves[x * 4 + y] if (x + move[0], y + move[1]) not in pastmoves]
# def addkeymap(keymap, keyword):
#     if keyword[0] in keymap and len(keyword) < 17:
#         keymap[keyword[0]].add(keyword)
#     else:
#         keymap[keyword[0]] = {keyword}
# def solve(x, y, possiblekeys, maxlenkey, gotcha, pastmoves, curr, clen, grid):
#     curr += grid[x * 4 + y]
#     if curr in possiblekeys:
#         gotcha.add(curr)
#         return curr
#     if clen > maxlenkey:
#         return False
#     pastmoves.add((x, y))
#     for move in movevable(x, y, pastmoves):
#         res = solve(x + move[0], y + move[1], possiblekeys, maxlenkey, gotcha, pastmoves.copy(), curr, clen + 1, grid)
#         if res:return res
#     return False

# def main():
#     for w in range(int(input())):
#         input()
#         grid = ''.join([input() for _ in range(4)])
#         keymap = {}
#         gotcha = set()
#         for _ in range(int(input())):
#             addkeymap(keymap, input())
#         for i in range(4):
#             for j in range(4):
#                 try:
#                     possiblekeys = keymap[grid[4 * i + j]]
#                     maxkeylen = max(len(k) for k in possiblekeys) if possiblekeys else 0
#                     res = solve(i, j, possiblekeys, maxkeylen, gotcha, set(), '', 0, grid)
#                     if res:
#                         keymap[grid[4 * i + j]].remove(res)
#                 except KeyError:
#                     pass
#         print(f'Score for Boggle game #{w + 1}: {sum([1, 1, 2, 3, 5][len(found) - 3] if len(found) < 8 else 11 for found in gotcha)}')

# if __name__ == "__main__":
#     main()

# end = time()
# print(f"Total time elapsed: {end - start}")

# from time import time

# start=time()
# moves = {0: ((0, 1), (1, 0), (1, 1)), 1: ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1)), 2: ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1)), 3: ((0, -1), (1, 0), (1, -1)), 4: ((0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)), 5: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 6: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 7: ((0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1)), 8: ((0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)), 9: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 10: ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)), 11: ((0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1)), 12: ((0, 1), (-1, 0), (-1, 1)), 13: ((0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)), 14: ((0, 1), (0, -1), (-1, 0), (-1, -1), (-1, 1)), 15: ((0, -1), (-1, 0), (-1, -1))}
# def movevable(x,y,pastmoves):return [move for move in moves[x*4+y]if move not in pastmoves]
# def addkeymap(keymap,keyword):
#     if keyword[0]in keymap.keys() and len(keyword)<17:keymap[keyword[0]].add(keyword)
#     else:keymap[keyword[0]]={keyword}
# def solve(x,y,possiblekeys,maxlenkey,gotcha,pastmoves,curr,clen,grid):
#     curr += grid[x*4+y]
#     if curr in possiblekeys:
#         gotcha.add(curr)
#         return curr
#     if clen>maxlenkey:return False
#     pastmoves.add((x,y))
#     for move in movevable(x,y,pastmoves):
#         res = solve(x+move[0],y+move[1],possiblekeys,maxlenkey,gotcha,pastmoves.copy(),curr,clen+1,grid)
#         if res:
#             return res
#     return False

# for w in range(int(input())):
#     input()
#     grid = ''.join([input() for _ in range(4)])
#     keymap = dict()
#     gotcha = set()
#     for gogokeys in range(int(input())):
#         addkeymap(keymap,input())
#     for i in range(4):
#         for j in range(4):
#             try:
#                 possiblekeys = keymap[grid[4*i+j]]
#                 maxkeylen = max(len(k)for k in possiblekeys) if possiblekeys else 0
#                 res=''
#                 res = solve(i,j,possiblekeys,maxkeylen,gotcha,set(),res,0,grid)
#                 if res:
#                     keymap[grid[4*i+j]].remove(res)
#             except KeyError:
#                 pass
#     print(f'Score for Boggle game #{w+1}: {sum([1,1,2,3,5][len(found)-3]if len(found)<8 else 11 for found in gotcha)}')
# end=time()
# print(f"Total time elapsed: {end-start}")


# try 1
# moves = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
# def check(x,y,move):
#     return -1<x+move[0]<4 and -1<y+move[1]<4


# def solve(grid,keywords,max_len,curr,gotcha,x,y,pastmoves):
#     newcurr = curr + grid[x][y]
#     if len(curr)>max_len:return
#     if curr in keywords:gotcha.add(curr)
#     pastmoves.add((x,y))
#     for move in moves:
#         new_x, new_y = x + move[0], y + move[1]
#         if check(x, y, move) and (new_x, new_y) not in pastmoves:
#             solve(grid,keywords,max_len,newcurr,gotcha,x+move[0],y+move[1],pastmoves.copy())
            


# for w in range(int(input())):
#     input()
#     grid = [input()for i in range(4)]
    
#     keywords = set(input()for i in range(int(input())))
#     # start = time()
#     max_len = max(len(x)for x in keywords)
#     gotcha = set()
#     for x in range(4):
#         for y in range(4):
#             solve(grid,keywords,max_len,'',gotcha,x,y,set())
#     print(gotcha)
#     print(f'Score for Boggle game #{w+1}: {sum([1,1,2,3,5][len(found)-3]if len(found)<8 else 11 for found in gotcha)}')
#     # end = time()
#     # print(f"total time: {start - end}")