from math import sqrt

total, x, y = map(int,input().split(" "))

side = sqrt(x*x + y*y)

arr=[]

for i in range(total):
    arr.append(int(input()))

for i in range(total):
    if arr[i]<=side:
        print("DA")
    else:
        print("NE")
