# armystrengthhard
# Army Strength (Hard)

n=int(input())
for _ in" "*n:
    input()
    a,b=map(int,input().split())
    A,B=sorted([*map(int,input().split())]),sorted([*map(int,input().split())])
    p1=p2=0
    while p1!=len(A) and p2!=len(B):
        if A[p1]>=B[p2]:p2+=1
        else:p1+=1
    print("Godzilla"if p2==len(B)else"MechaGodzilla")