# Message
# https://open.kattis.com/problems/meddelande


n,m = map(int,input().split())
s = ""
for i in range(n):
    I = input()
    for j in range(m):
        if I[j]!='.':
            s+=I[j]
print(s)