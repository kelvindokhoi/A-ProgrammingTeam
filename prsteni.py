# prsteni

# input()
# def gcd(x,y):
#     if y>x:x,y=y,x
#     if x==0:return y
#     if y==0:return x
#     return gcd(y,x%y)
# a,*b,=map(int,input().split())
# n=[f'{a//gcd(a,x)}/{x//gcd(a,x)}' for x in b]
# print(*n,sep='\n')



import math;input();a,*b,=map(int,input().split());print(*[f'{a//(l:=math.gcd(a,x))}/{x//l}'for x in b],sep='\n')

# from math import *
# a=[*map(int,open(0))]
# print(*[f'{a[0]//(l:=gcd(a[0],x))}/{x//l}'for x in a[1:]],sep='\n')

# from math import *
# a=[*map(int,open(0).read().split())]
# print(*[f'{a[1]//(l:=gcd(a[1],x))}/{x//l}'for x in a[2::]],sep='\n')