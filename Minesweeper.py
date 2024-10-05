x,y, bombs = map(int, input().split(" "))

bombsite = [["." for _ in range(y)] for _ in range(x)]

for _ in range(bombs):
    bombX, bombY = map(int, input().split(" "))
    bombsite[bombX-1][bombY-1] = "*"
for i in range(x):
    temp = ""
    for j in range(y):
        temp += bombsite[i][j]
    print(temp)
