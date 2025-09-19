# Planting Trees
# https://open.kattis.com/contests/atp9uc/problems/plantingtrees

num_seed = int(input())
tree_grow_days = sorted([*map(int,input().split())],reverse=True)
day_buffer = 0
max_day = 0
for tree_days in tree_grow_days:
    day_buffer +=1
    max_day = max(max_day,tree_days+day_buffer)
print(max_day+1)
