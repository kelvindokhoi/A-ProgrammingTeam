def moveA(arr):
    arr[0],arr[1] = arr[1],arr[0]

def moveB(arr):
    arr[1],arr[2] = arr[2], arr[1]

def moveC(arr):
    arr[0],arr[2] = arr[2], arr[0]

arrInput = [x for x in input()]
arr = [1,0,0]

for i in range(len(arrInput)):
    if arrInput[i] == "A":
        moveA(arr)
    if arrInput[i] == "B":
        moveB(arr)
    if arrInput[i] == "C":
        moveC(arr)

for j in range(3):
    if arr[j] == 1:
        print(j+1)