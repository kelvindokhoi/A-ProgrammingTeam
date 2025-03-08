# Primary Arithmetic

from collections import deque
def ans(carry):
    if carry==0:
        return("No carry operation.")
    elif carry==1:
        return("1 carry operation.")
    else:
        return(f"{carry} carry operations.")
while True:
    num1, num2 = input().split()
    if num1=='0' and num2=='0':
        break
    q1,q2 = deque(num1),deque(num2)
    carry = 0
    doicarry=False
    while q1 and q2:
        n1,n2=int(q1.pop()),int(q2.pop())
        if doicarry:
            if n1+n2+1>9:
                carry+=1
            else:
                doicarry=False
        else:
            if n1+n2>9:
                carry+=1
                doicarry=True
    left=0
    if q1:
        left=q1.copy()
    if q2:
        left=q2.copy()
    while left:
        n3=int(left.pop())
        if doicarry:
            if n3+1>9:
                carry+=1
            else:doicarry=False

    print(ans(carry))

