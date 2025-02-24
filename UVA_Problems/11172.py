# 11172 - Relational Operator


for _ in [0]*int(input()):
    a,b=map(int,input().split())
    print('='if a==b else ['<','>'][a>b])
