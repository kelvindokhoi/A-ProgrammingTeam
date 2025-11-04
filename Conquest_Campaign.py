# Conquest Campaign
# https://open.kattis.com/contests/ue23kp/problems/conquestcampaign
from collections import deque
row, col, weak = map(int,input().split())

sending_troops = deque()
visited = set()
sending_set = set()
# enemy_map = [[0]*col for _ in ' '*row]

for _ in ' '*weak:
    x,y=map(lambda x:int(x)-1,input().split())
    sending_troops.append((x,y,0))
    sending_set.add((x,y))

# def more_troops(data,visited=visited,row=row,col=col,sending_set=sending_set,enemy_map=enemy_map):
def more_troops(data,visited=visited,row=row,col=col,sending_set=sending_set):
    x,y,step = data
    # enemy_map[x][y] = step
    visited.add((x,y))
    points = []
    for i in range(2):
        possible_point_x,possible_point_y = x+(-1)**i,y
        if -1<possible_point_x<row and -1<possible_point_y<col:
            point = (possible_point_x,possible_point_y)
            if point not in visited:
                if point not in sending_set:
                    sending_set.add(point)
                    points.append((*point,step+1))

    for j in range(2):
        possible_point_x,possible_point_y = x,y+(-1)**j
        if -1<possible_point_x<row and -1<possible_point_y<col:
            point = (possible_point_x,possible_point_y)
            if point not in visited:
                if point not in sending_set:
                    sending_set.add(point)
                    points.append((*point,step+1))
    return points

max_step = 0
while sending_troops:
    current_troop = sending_troops.popleft()
    new_troops = more_troops(current_troop)
    if new_troops:
        max_step = max(max_step,new_troops[0][2])
    for new_troop in new_troops:
        sending_troops.append(new_troop)

print(max_step+1)
# for line in enemy_map:
#     print(line)




