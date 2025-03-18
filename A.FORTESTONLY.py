cases,length = map(int,input().split())
string_map = []
pos = [[[]for _ in' '*length]for _ in' '*(cases)]
for i in range(cases):
    curr_case = input()
    string_map.append(curr_case)
    for j in range(length):
        pos[i][ord(curr_case[j])-65]=j
choices=[*range(length)]
choices.sort(key= lambda x: (sum(pos[i][x] for i in range(cases)),max(pos[i][x] for i in range(cases))))
# print(pos)
# print(string_map)
def one_instance(first):
    curr_choises = [first]+[x for x in choices if x!=first]
    dp = [[0 for _ in range(cases+1)] for _ in range(length+1)]
    dp[0]=[0]+[-1]*cases
    n=0
    for choice in curr_choises:
        options = [pos[i][choice] for i in range(cases)]
        if all(x>y for x,y in zip(options,dp[n][1:])):
            dp[n+1]=[dp[n][0]+1]+options
        else:
            dp[n+1]=dp[n]
        n+=1
    return dp[length][0]

print(max(one_instance(i) for i in range(length)))