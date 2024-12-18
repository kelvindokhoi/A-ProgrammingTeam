# judgingmoose

n,p=map(int,input().split())

if n!=0 or p!=0:
    if n==p:
        print(f"Even {n*2}")
    else:
        print(f"Odd {(n,p)[p>n]*2}")
else:
    print("Not a moose")