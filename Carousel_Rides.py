# Carousel Rides
# carousel

while (inp:=input())!='0 0':
    n,m = map(int,inp.split())
    deals = []
    for i in range(n):
        ticket,price = map(int,input().split())
        if ticket<=m:
            deals.append((price/ticket,-ticket,price))
    if deals:
        deals.sort()
        print(f'Buy {-deals[0][1]} tickets for ${deals[0][2]}')
    else:
        print('No suitable tickets offered')
