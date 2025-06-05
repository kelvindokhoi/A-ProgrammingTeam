from decimal import*

for _ in[0]*int(input()):
    r,b,m= map(Decimal,input().split())
    r /= 100
    if (b*r).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)-m>=0:print('impossible');continue
    for i in range(1200):
        b += (b*r).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) - m
        if b<=0:break
    print(i+1 if b<=0 else'impossible')