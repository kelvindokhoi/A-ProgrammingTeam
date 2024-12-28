# volim

t=210
k=[]
i=int(input())-1
q=int(input())
for _ in' '*q:
    a,b=input().split()
    t-=int(a)
    if t<0:
        k.append(i+1)
    elif t==0:
        k.append(i+2)
    if b=="T":
        i=(i+1)%8
print(k[0])