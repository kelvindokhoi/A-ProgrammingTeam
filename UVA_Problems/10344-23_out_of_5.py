# 23 out of 5



# from time import time
# start = time()
# def solve(array, res, calc, count):
#     if count == 5:return res == 23
#     if calc == 0:res += array[count]
#     elif calc == 1: res -= array[count]
#     else:res *= array[count]
#     for i in range(3):
#         if solve(array, res, i, count + 1):
#             return True
#     return False

# def rbPermu(array, choices):
#     if len(array) != 5:
#         for i, item in enumerate(choices):
#             if rbPermu(array + [item], choices[:i] + choices[i + 1:]):
#                 return True
#     else:
#         if solve(array, 0, 0, 0):
#             return True
#     return False

# n = list(map(int, input().split()))
# stop = [0, 0, 0, 0, 0]
# while n != stop:
#     if n[0]==n[1]==n[2]==n[3]==n[4]:
#         if solve(n,0,0,0):
#             pass
#             # print('Possible')
#         else:
#             pass
#             # print('Impossible')
#     else:
#         if rbPermu([], n):
#             pass
#             # print('Possible')
#         else:
#             pass
#             # print('Impossible')
#     n = list(map(int, input().split()))

# end = time()
# print(f'total time: {end-start}')



def solve(array, res, calc, count):
    if count == 5:return res == 23
    if calc == 0:res += array[count]
    elif calc == 1: res -= array[count]
    else:res *= array[count]
    for i in range(3):
        if solve(array, res, i, count + 1):
            return True
    return False

def rbPermu(array, choices):
    if len(array) != 5:
        for i, item in enumerate(choices):
            if rbPermu(array + [item], choices[:i] + choices[i + 1:]):
                return True
    else:
        if solve(array, 0, 0, 0):
            return True
    return False

n = list(map(int, input().split()))
stop = [0, 0, 0, 0, 0]
while n != stop:
    if n[0]==n[1]==n[2]==n[3]==n[4]:
        if solve(n,0,0,0):
            print('Possible')
        else:
            print('Impossible')
    else:
        if rbPermu([], n):
            print('Possible')
        else:
            print('Impossible')
    n = list(map(int, input().split()))