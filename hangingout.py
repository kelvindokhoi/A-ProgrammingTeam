# hangingout
# Hanging Out on the Terrace

L,x=map(int,input().split());p=d=0
for i in" "*x:
    a,b=input().split();b=int(b)
    if"enter"==a:
        if p+b>L:d+=1
        else:p+=b
    else:
        p-=b
print(d)