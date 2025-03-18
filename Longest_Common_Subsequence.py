# Longest Common Subsequence


# original AC:
# cases,length = map(int,input().split())
# string_map = []
# pos = [[[]for _ in' '*length]for _ in' '*(cases)]
# for i in range(cases):
#     curr_case = input()
#     string_map.append(curr_case)
#     for j in range(length):
#         pos[i][ord(curr_case[j])-65]=j
# choices=[*range(length)]
# choices.sort(key= lambda x: (sum(pos[i][x] for i in range(cases)),max(pos[i][x] for i in range(cases))))
# def one_instance(first):
#     curr_choises = [first]+[x for x in choices if x!=first]
#     dp = [[0 for _ in range(cases+1)] for _ in range(length+1)]
#     dp[0]=[0]+[-1]*cases
#     n=0
#     for choice in curr_choises:
#         options = [pos[i][choice] for i in range(cases)]
#         if all(x>y for x,y in zip(options,dp[n][1:])):
#             dp[n+1]=[dp[n][0]+1]+options
#         else:
#             dp[n+1]=dp[n]
#         n+=1
#     return dp[length][0]

# print(max(one_instance(i) for i in range(length)))


# optimized by early termination, remove string_map, remove the tiebreaker in the sorting, and reuse the sorted choices instead of making new ones (0.14s):
cases, length = map(int, input().split())
pos = [[0] * length for _ in range(cases)]
for i in range(cases):
    curr_case = input()
    for j in range(length):
        pos[i][ord(curr_case[j]) - 65] = j

choices = [*range(length)]
choices.sort(key=lambda x: sum(pos[i][x] for i in range(cases)))

def one_instance(first, best_so_far):
    curr_choices = [first] + [x for x in choices if x != first]
    dp = [[0] * (cases + 1) for _ in range(length + 1)]
    dp[0] = [0] + [-1] * cases
    n = 0
    for choice in curr_choices:
        if dp[n][0] + (length - n) <= best_so_far:  # Early exit
            return dp[n][0]
        options = [pos[i][choice] for i in range(cases)]
        if all(x > y for x, y in zip(options, dp[n][1:])):
            dp[n+1] = [dp[n][0] + 1] + options
        else:
            dp[n+1] = dp[n]
        n += 1
    return dp[n][0]

best = 0
for i in range(length):
    best = max(best, one_instance(i, best))
print(best)

