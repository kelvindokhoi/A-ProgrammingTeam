# 11805 - Bafana Bafana
p=[]
for _ in range(o:=int(input())):
    N,K,P=map(int,input().split())
    p.append(a if(a:=(K+P)%N) else N)
for x in range(o):
    print(f"Case {x+1}: {p[x]}")