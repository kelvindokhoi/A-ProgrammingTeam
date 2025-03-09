# Spiderman's Workout

for _ in range(int(input())):
    num_moves = int(input())
    move_map = map(int,input().split())
    max_height = sum(move_map)
    dp_map = [[float('inf')]*(max_height+1) for _ in ' '*(num_moves+1)]
    choice = [['']*(max_height+1) for _ in ' '*(num_moves+1)]
    dp_map[0][0] = 0
    for i in range(1,num_moves+1):
        distance = move_map[i-1]
        for j in range(1,max_height):
            if j>=distance:
                newmax = max(dp_map[i-1][j-distance],j)
                if newmax < dp_map[i][j]:
                    dp_map[i][j] = newmax
                    choice[i][j] = 'U'
            if j+distance<= max_height:
                newmax = max(dp_map[i-1][j+distance],j+distance)
                if newmax < dp_map[i][j]:
                    dp_map[i][j] = newmax
                    choice[i][j] = 'D'
                    


