# Geppetto

total_ingredients, total_unmatch = map(int,input().split())
total_pizza = 1<<total_ingredients
# minus = 1<<total_ingredients-2
groups = set()
len_group = 0
for _ in' '*total_unmatch:
    m,n = map(int,input().split())
    if m>n:
        groups.add((~-n,~-m))
    else:
        groups.add((~-m,~-n))
groups = list(groups)
count = 0
for i in range(total_pizza):
    vibe_checked = True
    for pair in groups:
        if (i&(1<<pair[0]))and(i&(1<<pair[1])): 
            vibe_checked = False
            break
    if vibe_checked:
        count+=1
print(count)