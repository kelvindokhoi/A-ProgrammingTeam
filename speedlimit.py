# speedlimit

# def avr(a,b):
#     sum=b[0][0]*b[0][1]
#     for i in range(1,a):
#         sum+=b[i][0]*(b[i][1]-b[i-1][1])
#     return sum

# a=int(input())
# while a!=-1:
#     b=[[*map(int,input().split())] for _ in range(a)]
#     print(avr(a,b),"miles")
#     a=int(input())


# while (a:=int(input()))!=-1:
#     sum=0
#     prev=0
#     for i in range(a):
#         n=[*map(int,input().split())]
#         sum+=int(n[0])*(int(n[1])-prev)
#         prev=n[1]
#     print(sum,"miles")

while(n:=int(input()))>-1:b=[[*map(int,input().split())]for _ in' '*n];print(b[0][0]*b[0][1]+sum(x[0]*(x[1]-p[1])for x,p in zip(b[1:],b)),'miles')

# while(n:=int(input()))>-1:b=[[*map(int,input().split())]for i in range(n)];print(b[0][0]*b[0][1]+sum(x[0]*(x[1]-y[1])for x,y in zip(b[1:],b)),'miles')
# while(n:=int(input()))>-1:b=[[*map(int,input().split())]for _ in' '*n];print(b[0][0]*b[0][1]+sum(x[0]*(x[1]-p[1])for x,p in zip(b[1:],b)),'miles')


