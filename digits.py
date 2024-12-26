# digits
def roll(x,step):
    if x!="1":
        return roll(str(len(x)),step+1)
    else:
        return str(step+1)

while (n:=input())!="END":
    print(roll(n,0))