# for _ in' '*int(input()):a=[*map(int,input().split())];print(sum((b-c*2)*(b>c*2)for c,b in zip(a,a[1:])))

# for _ in' '*int(input()):*a,=map(int,input().split());print(sum((y-x*2)*(y>x*2)for x,y in zip(a,a[1:])))

exec("*a,=map(int,input().split());print(sum((y-x*2)for x,y in zip(a,a[1:])if y>x*2));"*int(input()))