# Battleship
# battleship

# python Battleship.py < Battleship_in.txt > Battleship_out.txt

# If p1 hits, and there's more ships, then p1 continue
# Branched?
# The game finished when every part of every ships got hit. (1)
# Hitting twice at a spot counts as a miss.
# If a ship got hit, it is counted as a sunked ship. But the game continues until (1) or it is a draw: both p1 and p2 navies are sunk, or if there's still ship left afterwards.

# Function for detecting ships
def Get_Ships(width:int,height:int):
    Ships = set()
    for y in range(height):
        for x,c in enumerate(input().rstrip()):
            if c=='#':
                Ships.add((x,height-1-y))
    return Ships

# Input 
test_cases = int(input())
for case_nth in range(test_cases):
    width, height, shots = map(int,input().split())
    Ships = (Get_Ships(width,height),Get_Ships(width,height))

    # For simplicity, let's assume p1 go first. Assumption changed?
    current_turn = False
    dump = False

    for shot_nth in range(shots):
        x,y = map(int,input().split())
        if dump:
            continue
        if (x,y) in Ships[not current_turn]:
            Ships[not current_turn].remove((x,y))
            if not Ships[not current_turn]:
                if current_turn:
                    dump = True
                else:
                    current_turn = not current_turn
        elif current_turn and not Ships[current_turn]:
                dump = True
        else:
            current_turn = not current_turn

    if all(Ships) or not any(Ships):
        print('draw')
    elif Ships[0]:
        print('player one wins')
    else:
        print('player two wins')

# Golfed Ver.:
# def G(h):return{(x,h-1-y)for y in range(h)for x,c in enumerate(input())if c=='#'}
# for _ in[0]*int(input()):
#  w,h,s=map(int,input().split());S=[G(h),G(h)];t=d=0
#  for _ in[0]*s:
#   x,y=map(int,input().split())
#   if d:continue
#   if(x,y)in S[~t]:S[~t].discard((x,y));d=not S[~t]and t;t|=not S[~t]
#   elif t and not S[t]:d=1
#   else:t=~t
#  print('draw'if all(S)or not any(S)else f"player %s wins"%('one'if S[0]else'two'))