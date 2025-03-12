# Climbing Worm
# climbingworm

up,down,total = map(int,input().split())
one_cycle = up-down
num_cycle = (total-up)//one_cycle
if up>=total:
    print(1)
else:
    print(num_cycle+1)

# a,b,c=map(int,input().split());print(+(a>c)or(c+~a)//(a-b)+2)