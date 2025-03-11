# Fast Food Prizes
# fastfood
def enough(curr,req):
    for x in req:
        if curr[x]==0:
            return False
    return True

for _ in range(int(input())):
    n,m = map(int,input().split())
    # n is number of prizes, m is number of stickers
    prizes=[[] for _ in range(n)]
    for i in range(n):
        _,*reqticktets,cash = map(int,input().split())
        prizes[i]=[cash,reqticktets]
    temp = [*map(int,input().split())]
    tickets = {i:temp[i-1] for i in range(1,m+1)}
    prizes.sort(key=lambda x:x[0],reverse=True)
    cash_sum = 0
    for prize in prizes:
        while enough(tickets,prize[1]):
            cash_sum+=prize[0]
            for reqt in prize[1]:
                tickets[reqt]-=1
    print(cash_sum)



