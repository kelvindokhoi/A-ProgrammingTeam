# peasoup
# Pea Soup and Pancakes

n=int(input())  #number of restaurants
res=[]
for i in" "*n:
    #check menus
    items=int(input())
    name=input()
    ps=pc=0
    for _ in" "*items:
        a=input()
        if a=="pea soup":
            ps+=1
        if a=="pancakes":
            pc+=1
    if ps and pc:
        res.append(name)
print(res[0]if res else"Anywhere is fine I guess")