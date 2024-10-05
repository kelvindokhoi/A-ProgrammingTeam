y,x, larY, larX = map(int, input().split(" "))

arr = [[i for i in input()] for _ in range(y)]

for j in range(y):
    for plusY in range(larY):
        tempStr = ""
        for i in range(x):
            for plusX in range(larX):
                tempStr += arr[j][i]
        print(tempStr)