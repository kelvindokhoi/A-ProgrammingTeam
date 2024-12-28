# acm
m=[]
while(n:=input())!="-1":
    m+=[n.split()]
k=len(m)
totalSolved=0
time=0
for i in range(k):
    if m[i][2]=="right":
        totalSolved+=1
        time += sum([20 for a in m if a[1]==m[i][1]]) - 20 + int(m[i][0])
print(totalSolved,time)
