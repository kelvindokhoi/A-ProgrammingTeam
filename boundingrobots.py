# boundingrobots

def move(init,value,bound):
    if init+value>bound:
        return bound
    if init+value<0:
        return 0
    return init+value
while (Z:=input())!="0 0":
    w,l=[i-1 for i in map(int,Z.split())]
    n=int(input())
    a=b=0 #robot
    x=y=0 #real
    for _ in" "*n:
        t1,t2=input().split()
        t2=int(t2)
        if t1=="r":
            a+=t2
            x=move(x,t2,w)
        if t1=="l":
            a-=t2
            x=move(x,-t2,w)
        if t1=="u":
            b+=t2
            y=move(y,t2,l)
        if t1=="d":
            b-=t2
            y=move(y,-t2,l)
    print(f"Robot thinks {a} {b}")
    print(f"Actually at {x} {y}")


