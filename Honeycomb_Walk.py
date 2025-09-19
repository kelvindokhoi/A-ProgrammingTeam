# Honeycomb Walk
# https://open.kattis.com/contests/hd35qb/problems/honey


#No solution yet
solution = dict(zip(range(1,15),[0]*14))

def move(current_comb,total_move_made,desired_move_made):
    print(current_comb)
    if total_move_made>desired_move_made:
        return 0
    if total_move_made==desired_move_made and current_comb==(0,0):
        return 1
    # if abs(current_comb[0])+abs(current_comb[1])>desired_move_made-total_move_made:
    #     return 0
    total = 0
    total_move_made += 1
    for x in [-1,1]:
        for y in [0,1,2]:
            new_comb = (current_comb[0]+x,current_comb[1]+x*y)
            total += move(new_comb,total_move_made,desired_move_made)
    return total


for i in range(1,3):
    solution[i] = move((0,0),0,i)
print(solution)
