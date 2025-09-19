# Pizzubestun
# https://open.kattis.com/contests/hd35qb/problems/pizzubestun

num_pizz = int(input())
pizzas = []
for _ in' '*num_pizz:
    name,price = input().split()
    pizzas.append((int(price),name))
pizzas.sort(reverse=True)
cost = 0
for i in range(num_pizz//2):
    cost += pizzas[i*2][0]
if num_pizz&1:
    cost +=pizzas[-1][0]
print(cost)