# Harshad Numbers
n = int(input())
def f(s):
    n = 0
    for c in s:
        n+=int(c)
    return n
for i in range(n,n*10):
    if i%f(str(i))==0:
        print(i)
        break
    