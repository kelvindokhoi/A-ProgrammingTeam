# Gluttonous George

# https://open.kattis.com/problems/goggi

a,_,b = input().split()
a,b=int(a),int(b)
if a>b:
    print('>')
elif a<b:
    print("<")
else:
    print("Goggi svangur!")