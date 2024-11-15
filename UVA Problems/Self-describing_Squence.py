from bisect import bisect_left

answer = []

#premake answer
allans = [0,1,3]
tempPoint = 3
while allans[-1] <= 2e9:
    allans.append(allans[tempPoint-1]+bisect_left(allans,tempPoint))
    tempPoint +=1


def findval(n):
    return bisect_left(allans,n)


first = int(input())

while first:
    answer.append(findval(first))
    first = int(input())

for length in range(len(answer)):
    print(answer[length])