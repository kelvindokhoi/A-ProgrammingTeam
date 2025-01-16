# Which Base is it Anyway?

# i,m=int,1;*n,=map(str,open(0).read().split())
# for _ in' '*i(n[0])//2:
#     try:p=i(n[m+1],8)
#     except:p=0
#     print(n[m],p,i(n[m+1]),i(n[m+1],16));m+=2
# exec('try:p=i(n[-~m],8)\nexcept:p=0\nprint(n[m],p,i(n[-~m]),i(n[-~m],16));m+=2;'*int(n[0]))

# i,j=int,input;exec('a,k=map(str,j().split())\ntry:p=i(k,8)\nexcept:p=0\nprint(a,p,i(k),i(k,16));'*i(j()))


i,j=int,input;exec('a,k=map(str,j().split());print(a,0 if{*"89"}&{*k}else i(k,8),i(k),i(k,16));'*i(j()))

i,j=int,input
for _ in' '*i(j()):
 a,k=map(str,j().split())
 print(a,0 if{*"89"}&{*k}else i(k,8),i(k),i(k,16))

 
