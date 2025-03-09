# Spiderman's Workout

for _ in range(int(input())):
    num_moves = int(input())
    move_map = [*map(int,input().split())]
    max_height = sum(move_map)
    dp_map = [[float('inf')]*(max_height+1) for _ in ' '*(num_moves+1)]
    choice = [['']*(max_height+1) for _ in ' '*(num_moves+1)]
    dp_map[0][0] = 0
    for i in range(1,num_moves+1):
        value = move_map[i-1]
        for j in range(max_height+1):
            # move up
            if j>=value:
                new_max_height = max(dp_map[i-1][j-value],j)
                if dp_map[i-1][j-value]!=float('inf') and new_max_height<dp_map[i][j]:
                    dp_map[i][j]=new_max_height
                    choice[i][j]='U'
            #move down
            if j+value<=max_height:
                new_max_height = max(dp_map[i-1][j+value],j+value)
                if dp_map[i-1][j+value]!=float('inf') and new_max_height<dp_map[i][j]:
                    dp_map[i][j]=new_max_height
                    choice[i][j]='D'
    if dp_map[num_moves][0]!=float('inf'):
        outputstring = ''
        curr_height = 0
        for k in range(num_moves,0,-1):
            value = move_map[k-1]
            if choice[k][curr_height]=='U':
                outputstring+='U'
                curr_height-=value
            else:
                outputstring+='D'
                curr_height+=value
        print(outputstring[::-1])
    else:
        print('IMPOSSIBLE')

# golfed:
# M,R,G,H,P=max,range,int,input,print
# for _ in' '*G(H()):
#  n,m=G(H()),[*map(G,H().split())];h=-~sum(m);d,c=[1e3]*h*-~n,['']*h*-~n;d[0]=0
#  for i in R(1,-~n):
#   for j in R(h):
#    O,v,I=i*h+j,m[~-i],h*~-i+j
#    if(w:=M(d[I-v],j))<d[O]:d[O],c[O]=w,c[I-v]+'U'
#    if j+v<h and(q:=M(d[I+v],j+v))<d[O]:d[O],c[O]=q,c[I+v]+'D'
#  print(c[n*h]if d[n*h]-1e3 else'IMPOSSIBLE')