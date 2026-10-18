# 10130 - SuperSale
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1071
# Test: python UVA_Problems/10130-SuperSale.py < UVA_Problems/10130-SuperSale_in.txt

def solve():
    N_objects = int(input())
    O_object_list = []
    for _ in range(N_objects):
        P_price, W_weight = map(int,input().split())
        O_object_list.append((W_weight,P_price))
    G_num_people = int(input())
    GMW_G_max_weight = []
    for _ in range(G_num_people):
        MW_max_weight = int(input())
        GMW_G_max_weight.append(MW_max_weight)
    GMW_G_max_weight.sort()
    O_object_list.sort()
    SMP_sum_max_price = 0
    for P_person in GMW_G_max_weight:
        SMP_sum_max_price += modified_2d_knapsack(P_person,O_object_list)
    print(SMP_sum_max_price)

# def dp_knapsack_solve(O_object_list,MW_max_weight):
#     dp_obj = [0 for _ in range(MW_max_weight+1)]
#     MP_max_price = 0
#     chosen_items = []
#     for i in range(1,len(O_object_list)+1):
#         for j in range(MW_max_weight,O_object_list[i-1][0]-1,-1):
#             new_val = dp_obj[j-O_object_list[i-1][0]] + O_object_list[i-1][1]
#             if new_val>dp_obj[j]:
#                 dp_obj[j] = new_val
#                 MP_max_price +=  O_object_list[i-1][1]
#     return MP_max_price

def modified_2d_knapsack(W, obj):
    n = len(obj)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(n + 1):
        for j in range(W + 1):

            # If there is no item or the knapsack's capacity is 0
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                pick = 0

                # Pick ith item if it does not exceed the capacity of knapsack
                if obj[i - 1][0] <= j:
                    pick = obj[i - 1][1] + dp[i - 1][j - obj[i - 1][0]]

                # Don't pick the ith item
                notPick = dp[i - 1][j]

                dp[i][j] = max(pick, notPick)

    chosen = []
    curr_ind = n
    curr_weight = W
    while curr_ind>0:
        if dp[curr_ind][curr_weight] != dp[curr_ind-1][curr_weight]:
            chosen.append(curr_ind-1)
            curr_weight -= obj[curr_ind-1][0]
        curr_ind -= 1
    
    MS_max_sum = 0
    for ind in chosen:
        v = obj.pop(ind)
        MS_max_sum += v[1]

    return MS_max_sum

T_cases = int(input())
for _ in range(T_cases):
    solve()