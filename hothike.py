# hothike

a=int(input())
n=[*map(int,input().split())]
M=50;p=0
for i in range(a-2):
    if M>max(n[i],n[i+2]):
        M=max(n[i],n[i+2])
        p=i+1
print(p,M)