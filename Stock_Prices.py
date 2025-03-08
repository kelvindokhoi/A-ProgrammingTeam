# Stock Prices

import heapq

def checkbuy(buy):
    return -buy[0][0] if buy else '-'
def checksell(sell):
    return sell[0][0] if sell else '-'
def checkstockprice(stockprice):
    return stockprice if stockprice != -1 else '-'

def establishadeal(buy,sell):
    lastprice=-1
    while buy and sell and -buy[0][0] >= sell[0][0]:
        buyprice,buyquantity = heapq.heappop(buy)
        sellprice,sellquantity = heapq.heappop(sell)
        lastprice=sellprice
        
        if buyquantity<sellquantity:
            heapq.heappush(sell,(sellprice,sellquantity-buyquantity))
        if sellquantity<buyquantity:
            heapq.heappush(buy,(buyprice,buyquantity-sellquantity))
    return lastprice

cases =int(input())
for i in range(cases):
    buy = [];heapq.heapify(buy)
    sell = [];heapq.heapify(sell)
    stockprice = -1
    ops = int(input())
    for op in range(ops):
        command,quantity,_,_,price = input().split()
        quantity,price=int(quantity),int(price)
        if command=='buy':
            heapq.heappush(buy,(-int(price),int(quantity)))
        else:
            heapq.heappush(sell,(int(price),int(quantity)))
        newdeal = establishadeal(buy,sell)
        stockprice = stockprice if newdeal==-1 else newdeal
        print(checksell(sell),checkbuy(buy),checkstockprice(stockprice))

# golfed code (obsfucated)
# from heapq import*;I,H,P,R=input,heappush,heappop,int
# for _ in' '*R(I()):
#  b,s,p=[],[],-1
#  for _ in' '*R(I()):
#   c,q,_,_,r=I().split()
#   if'c'>c:H(b,(-R(r),R(q)))
#   else:H(s,(R(r),R(q)))
#   d=-1
#   while b and s and -b[0][0]>=s[0][0]:x,y=P(b);z,w=P(s);d=z;y>=w or H(s,(z,w-y));w>=y or H(b,(x,y-w))
#   p=[d,p][d<0];print(s and s[0][0]or'-',b and-b[0][0]or'-',['-',p][p>0])

# shortest
# from heapq import*;I,H,P,R=input,heappush,heappop,int
# for _ in' '*R(I()):b,s,p=[],[],-1;exec("c,q,_,_,r,d=*I().split(),-1;H(b,(-R(r),R(q)))if'c'>c else H(s,(R(r),R(q)))\nwhile b and s and -b[0][0]>=s[0][0]:x,y=P(b);z,w=P(s);d=z;y>=w or H(s,(z,w-y));w>=y or H(b,(x,y-w))\np=[d,p][d<0];print(s and s[0][0]or'-',b and-b[0][0]or'-',['-',p][p>0]);"*R(I()))