# 10071 - Back to High School Physics
# def p():
#     a,b=map(int,input().split())
#     return a*b<<1
# print(*[p() for _ in range(2)],sep="\n")

# while (a:=input()):print(*[ eval('*2*'.join(a.split()))],sep="\n")

# golfing:
# while 1:
#  try:print(eval('*'.join(input().split()))*2)
#  except:break

# time optimization
import sys

while True:
    try:
        line = sys.stdin.readline()
        a, b = int(line.split()[0]), int(line.split()[1])
        print(a * b * 2)
    except IndexError: #don't use EOFError becuz here: a, b = int(line.split()[0]), int(line.split()[1]) has index accessing
        break