# Battleship
# battleship

# python Battleship.py < Battleship_in.txt > Battleship_out.txt

# what if there is no ship in the beginning
# we need to simulate case where p1 starts first and case where p2 starts first

def play(p1_points,p2_points,shoots,p1_turn):
    p1start = 'u'
    for p in shoots:
        len1 = len(p1_points)
        len2 = len(p2_points)
        if len1==0 and len2==0:
            p1start = 'd'
            break
        if len1==0:
            p1start = '2'
            break
        if len2==0:
            p1start = '1'
            break
        if p1_turn:
            p1_points.discard(p)
            p1_turn = 0
        else:
            p2_points.discard(p)
            p1_turn = 1
    return p1start


for tc in range(int(input())):
    w,h,n = map(int,input().split())
    p1_map = [input() for _ in ' '*h]
    p2_map = [input() for _ in ' '*h]
    p1_points = set()
    p2_points = set()
    # can be optimized later if TLE 
    for i in range(h):
        for j in range(w):
            if p1_map[i][j]=='#':
                p1_points.add((j,i))
            if p2_map[i][j]=='#':
                p2_points.add((j,i))
    # shooting begins
    shoots = [tuple([*map(int,input().split())])for _ in ' '*n]
    # if p1 is the starter
    result1 = play(p1_points.copy(),p2_points.copy(),shoots,1)
    # print(p1_points,p2_points)
    result2 = play(p1_points,p2_points,shoots,0)
    if result1==result2:
        if result1=='d' or result1=='u':
            print('draw')
        elif result1=='1':
            print('player one wins')
        else:
            print('player two wins')
    else:
        if result1=='u':
            if result2=='d':
                print('draw')
            elif result2=='1':
                print('player one wins')
            else:
                print('player two wins')
        elif result2=='u':
            if result1=='d':
                print('draw')
            elif result1=='1':
                print('player one wins')
            else:
                print('player two wins')
        elif result1=='d':
            if result2=='1':
                print('player one wins')
            else:
                print('player two wins')
        elif result2=='d':
            if result1=='1':
                print('player one wins')
            else:
                print('player two wins')
        else:
            print('draw')
    # print(result1,result2)



