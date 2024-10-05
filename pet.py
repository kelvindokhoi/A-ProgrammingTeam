mapper = [[x for x in input().split(" ")] for _ in range(5)]

maxPoint = -1
winnerPos = -1

for i in range(5):
    point = sum([int(x) for x in mapper[i]])
    if point > maxPoint:
        maxPoint = point
        winnerPos = i

print(winnerPos + 1, maxPoint)