# Password Hacking

numpas = int(input())
pw = []
for _ in ' '*numpas:
    pw.append(float(input().split()[1]))
pw.sort(reverse=True)
sum = 0
for i in range(numpas):
    sum+=(i+1)*pw[i]
print(sum)