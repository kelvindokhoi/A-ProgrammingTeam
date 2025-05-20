# Modular Arithmetic
# python Modular_Arithmetic.py < Modular_Arithmetic_in.txt


# (a/b)%m = (a*b^-1)%m
# modular inverse is x such that bx=1(mod m). B will have modInverse iff a and m are coprime
def extEuclid(a,b):
    x,y, u,v = 0,1, 1,0
    while a!=0:
        q,r = b//a, b%a
        m,n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r ,u,v ,m,n
    gcd = b
    return gcd,x,y

def modInverse(b,m):
    d,i,j = extEuclid(b,m)
    if d!=1:
        return -1
    return i%m

while 1:
    n,t = map(int,input().split())
    if n==t==0:
        exit()
    for _ in range(t):
        a,op,b = input().split()
        a,b = int(a),int(b)
        if op=='/':
            new_b = modInverse(b,n)
            print((a*new_b)%n if new_b!=-1 else -1)
        if op=='+':
            print((a+b)%n)
        if op=='-':
            print((a-b)%n)
        if op=='*':
            print((a*b)%n)