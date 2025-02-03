# pivot


# a,*b=map(int,open(0).read().split());M,m,r=[b[0]],[b[-1]],range
# for i in r(1,a):M+=[max(b[i],M[i-1])];m+=[min(b[a+~i],m[i-1])]
# print(sum(M[i]<=m[a+~i]for i in r(a)))


a,*b=map(int,open(0).read().split());M,m=[b[0]],[b[-1]]
for i in range(1,a):M+=[max(b[i],M[i-1])];m+=[min(b[a+~i],m[i-1])]
print(sum(M[i]<=m[a+~i]for i in range(a)))

