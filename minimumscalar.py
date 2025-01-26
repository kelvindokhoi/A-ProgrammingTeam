# minimumscalar.py
# minimum scalar product

for i in range(int(input())):
    input();a=[*map(int,input().split())];b=[*map(int,input().split())]
    a.sort(reverse=True);b.sort()
    print(f"Case #{i+1}: {sum([x*y for x,y in zip(a,b)])}")