# armystrengtheasy
# Army Strength (Easy)

n=int(input())
for _ in" "*n:
    input()
    a,b=map(int,input().split())
    A,B=sorted([*map(int,input().split())]),sorted([*map(int,input().split())])
    while A!=[]and[]!=B:
        if A[0]==B[0]:
            B.pop(0)
        else:[A.pop(0)if B[0]>A[0]else B.pop(0)]
    print("Godzilla"if A else"MechaGodzilla")