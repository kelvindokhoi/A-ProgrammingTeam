# Shattered Cake
# shatteredcake

w=int(input())
a=0
for i in range(int(input())):
    b,c=map(int,input().split())
    a+=b*c
print(a//w)