# Credit_Card_Payment.py


# creditcard
# https://open.kattis.com/problems/creditcard

# python Credit_Card_Payment.py < Credit_Card_Payment_in.txt

from decimal import Decimal, ROUND_HALF_UP

for i in range(int(input())):
    r,b,m = map(Decimal,input().split())
    if b<=0:
        print(0)
        continue
    r = r/100
    if (b*r).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)-m>=0:
        print('impossible')
        continue
    month_passed = 0
    for i in range(1200):
        month_passed += 1
        interest = (b*r).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        b = b + interest
        b = b - m 
        if b<=0:
            break
    if b<=0:
        print(month_passed)
    else:
        print('impossible')


# semi-golfed:
# from decimal import*

# for _ in[0]*int(input()):
#     r,b,m= map(Decimal,input().split())
#     r /= 100
#     if (b*r).quantize(Decimal('0.01'),rounding=ROUND_HALF_UP)-m>=0:print('impossible');continue
#     for i in range(1200):
#         b += (b*r).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP) - m
#         if b<=0:break
#     print(i+1 if b<=0 else'impossible')