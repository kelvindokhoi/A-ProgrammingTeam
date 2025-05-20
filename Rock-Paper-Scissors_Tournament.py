# Rock-Paper-Scissors Tournament
# rockpaperscissors

# python Rock-Paper-Scissors_Tournament.py
while (i:=input())!='0':
    n,k = map(int,i.split())
    players = [{'w':0,'l':0}for _ in' '*n]
    for _ in range((k*(n-1)*n)//2):
        p1,c1,p2,c2  = input().split()
        if c1==c2:continue
        if c1=='rock':
            if c2=='scissors':
                players[int(p1)-1]['w']+=1
                players[int(p2)-1]['l']+=1
            else:
                players[int(p1)-1]['l']+=1
                players[int(p2)-1]['w']+=1
        elif c1=='paper':
            if c2=='rock':
                players[int(p1)-1]['w']+=1
                players[int(p2)-1]['l']+=1
            else:
                players[int(p1)-1]['l']+=1
                players[int(p2)-1]['w']+=1
        else:
            if c2=='paper':
                players[int(p1)-1]['w']+=1
                players[int(p2)-1]['l']+=1
            else:
                players[int(p1)-1]['l']+=1
                players[int(p2)-1]['w']+=1
    for e in players:
        if e['w']+e['l']!=0:
            print('{:0.3f}'.format(e['w']/(e['w']+e['l'])))
        else:
            print('-')
    print()

