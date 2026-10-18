# Goomba Stacks
# https://open.kattis.com/problems/goombastacks

# n,s = int(input()),0
# for _ in' '*n:
#     g,b=map(int,input().split())
#     s+=g
#     if s<b and n!=0:
#         print("impossible")
#         n=0
# if n!=0:
#     print("possible")

O=input
n,s,t=int(O()),0,1
for i in range(n):
 z,x=map(int,O().split())
 s+=z
 t=t and (s+z<x)
print("im"*t+"possible")


