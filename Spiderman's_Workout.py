# Spiderman's Workout



from collections import deque
cases = int(input())
for i in range(cases):
    maxj = int(input())
    jumpmap = [*map(int,input().split())]
    myq = deque()
    myq.append((jumpmap[0],'U',0,jumpmap[0]))
    solutions = []
    while myq:
        currmax,currm,movetaken,currh = myq.popleft()
        if movetaken==7 and currh==0:
            solutions.append((currmax,currm))
        else:
            nexttaken = movetaken+1
            nextstep = jumpmap[nexttaken]
            

    currh=0
    currm = ''
    for move in jumpmap:
        if currh-move>=0:
            currm+='D'
            currh-=move
        else :
            currm+='U'
            currh+=move
    if currh==0:
        print(currm)
    else:
        print('IMPOSSIBLE')