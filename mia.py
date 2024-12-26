# mia

while (k:=input())!="0 0 0 0":
    a,b,c,d=map(int,k.split())
    p1=p2=0
    if {a,b}=={2,1}:
        p1=700
    elif a==b:
        p1=a*100+b*10
    else:
        p1=[a,b][b>a]*10+[a,b][b<a]
    if {c,d}=={2,1}:
        p2=700
    elif c==d:
        p2=c*100+d*10
    else:
        p2=[c,d][d>c]*10+[c,d][d<c]
    print("Tie." if p1==p2 else f"Player {[1,2][p2>p1]} wins.")
