# orders.py
# Restaurant Orders
# def knapsack(W, val, wt):
    
#     # Initializing dp list
#     dp = [0] * (W + 1)

#     # Taking first i elements
#     for i in range(1, len(wt) + 1):
        
#         # Starting from back, so that we also have data of
#         # previous computation of i-1 items
#         for j in range(W, wt[i - 1] - 1, -1):
#             dp[j] = max(dp[j], dp[j - wt[i - 1]] + val[i - 1])
    
#     return dp[W],dp
from itertools import combinations
allit = dict()
n_num_it = int(input())
val = [1 for _ in range(n_num_it)]
items = list(map(int,input().split()))
m_num_placed = int(input())
orders = list(map(int,input().split()))
for i in range(1,n_num_it+1):
    for j in combinations(items,i):
        if sum(j) in allit:
            allit[sum(j)].append(j)
        else:
            allit[sum(j)] = [j]
for W in orders:
    if W in allit:
        if len(allit[W])==1:
            print(' '.join(str(i) for i in allit[W][0]))
        else:
            print('Ambiguous')
    else:
        print("Impossible")
