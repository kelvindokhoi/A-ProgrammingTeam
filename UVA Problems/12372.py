# 12372 - Packing for Holiday


for i in range(int(input())):
    a,b,c=map(int,input().split())
    print(f"Case {i+1}: "+["bad","good"][(a<21)*(b<21)*(c<21)])