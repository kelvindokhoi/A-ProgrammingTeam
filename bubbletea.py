# bubbletea
# Delicious Bubble Tea

N=int(input()) #the amount of kinds of tea the shop has.
TeaPrice=[*map(int,input().split())] #the price of all kinds of tea.
M=int(input()) #the amount of toppings the shop has.
ToppingPrice=[*map(int,input().split())] #the price of all kinds of topping.
Mixing=[[*map(int,input().split())][1:]for _ in" "*N]
money=int(input())
combinedBoba={a:b for a,b in zip(range(1,M+1),ToppingPrice)}
combinedPrice=min([a+b for a,b in zip(TeaPrice,[min([combinedBoba[i] for i in a]) for a in Mixing])])
if money//combinedPrice>1:
    print(money//combinedPrice-1)
else:
    print(0)
