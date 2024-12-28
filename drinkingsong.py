# drinkingsong

a=int(input());b=input()
for i in range(a,1,-1):
    print(f"{i} bottles of {b} on the wall, {i} bottles of {b}.\nTake one down, pass it around, {i-1} bottle{'s'if i-2 else''} of {b} on the wall.\n")
print(f"1 bottle of {b} on the wall, 1 bottle of {b}.\nTake it down, pass it around, no more bottles of {b}.")