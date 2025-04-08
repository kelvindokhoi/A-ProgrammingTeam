# CD

# while True:
#     N,M = map(int,input().split())
#     if N==0 and M==0:break
#     Ncd = {int(input())for _ in' '*N}
#     Mcd = {int(input())for _ in' '*M}
#     print(len(Ncd & Mcd))

while 1:(M:=[*map(int,input().split())])!=[0,0]or exit();print(len({int(input())for _ in' '*M[0]}&{int(input())for _ in' '*M[1]}))