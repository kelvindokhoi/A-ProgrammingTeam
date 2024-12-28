# brokenswords

n=int(input())
a=b=0
k={"0":1,"1":0}
for i in" "*n:
    z=input()
    a+=k[z[0]]+k[z[1]]
    b+=k[z[2]]+k[z[3]]
x=min(a,b)//2
print(x,a-x*2,b-x*2)
