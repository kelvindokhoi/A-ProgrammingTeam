# abc

a,b,c=sorted(map(int,input().split()))
print(*[{"A":a,"B":b,"C":c}[i] for i in [*input()]])