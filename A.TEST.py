'''
totalStr = int(input())

array = [[[x for x in input()] for _ in range(2)] for _ in range(totalStr)]

arrAns = [[0] * len(array[0][0]) for _ in range(totalStr)]



print(arrAns)
'''

A = [(1,2,3)]
A = [*zip(*A)]
print(A)