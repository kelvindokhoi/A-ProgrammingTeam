# Weak Vertices

p,o,u=input,range,int
while(n:=u(p()))+1:a,_=[],[*o(n)];exec('m=[*map(u,p().split())];a.append([j for j in o(n) if m[j]]);'*n);[_:=[v for v in _ if v-i]for i in o(n)for j in a[i]for k in a[j]if i in a[k]];print(*_)


# p,o,u=input,range,int
# while(n:=u(p()))+1:
#  a,_=[],[*o(n)];exec('m=[*map(u,p().split())];a.append([j for j in o(n) if m[j]==1]);'*n)
#  for i in o(n):
#   for j in a[i]:
#    for k in a[j]:
#     if i in a[k]:_=[v for v in _ if v-i]
#  print(*_)
