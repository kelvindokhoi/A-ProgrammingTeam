def printArr(arr,totalStr):

    for x in range(totalStr):
        for y in range(3):
            tempStr = ""
            for z in range(len(arr[x][0])):
                tempStr += arr[x][y][z]
            print(tempStr)
        print("\n")



totalStr = int(input())

#input the data into a 3D array with the dimension of totalStr:2:len(input())
array = [[[x for x in input()] for _ in range(2)] for _ in range(totalStr)]

#append a 3rd in the 2nd dimension
for x in range(totalStr):
    array[x].append([None]*len(array[x][0]))



#check for differences between the 2 strings in a group
#for the sake of simplicity, x will be totalStr, y will be the string order, z will be the order of the single char
for x in range(totalStr):
    for y in range(2):
        for z in range(len(array[x][0])):
            if array[x][0][z] != array[x][1][z]:
                array[x][2][z] = "*"
            elif array[x][0][z] == array[x][1][z]:
                array[x][2][z] = "."


printArr (array, totalStr)
