# A Prize No One Can Win
# https://open.kattis.com/contests/atp9uc/problems/aprizenoonecanwin

num_i_for_sale, min_cost_X = map(int,input().split())
item_prices = sorted([*map(int,input().split())])
total_item_selected = 0

if num_i_for_sale<2:
    print(num_i_for_sale)
else:
    item_prices = [0]+item_prices
    for a,b in zip(item_prices,item_prices[1::]):
        if a+b>min_cost_X:
            continue
        total_item_selected +=1
    print(total_item_selected if total_item_selected>0 else 1)
