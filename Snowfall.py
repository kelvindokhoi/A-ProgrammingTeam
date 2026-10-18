n= 0
for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==1:
        n = max(0,n-b)
    else:
        n += b
print(n)