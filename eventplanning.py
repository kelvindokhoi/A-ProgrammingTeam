# eventplanning

participants,budget,hotels,weeks=map(int,input().split())
minPrice=1e7
for i in range(hotels):
    price=int(input())
    beds=[*map(int,input().split())]
    for j in range(weeks):
        if beds[j]>=participants:
            if price<minPrice:
                minPrice=price
ans=minPrice*participants
print(ans if ans<budget else 'stay home')