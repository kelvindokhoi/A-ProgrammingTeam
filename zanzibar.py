# zanzibar
# Stand on Zanzibar


for i in ' '*int(input()):
    a=[*map(int,input().split())]
    outlander=0
    for n in range(len(a)-1):
        outlander+=(a[n+1]-a[n]*2)*(a[n+1]>a[n]*2)
    print(outlander)

# exec("*a,=map(int,input().split());print(sum((y-x*2)for x,y in zip(a,a[1:])if y>x*2));"*int(input()))