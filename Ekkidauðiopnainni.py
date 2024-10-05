arr = [[x for x in input().split("|")] for _ in range(2)]
ans= ""
for x in range(2):
    for y in range(2):
        ans += arr[y][x]
    if x ==0:
        ans += " "

print(ans)