# Neighborhood Watch

# houses,neiborhood=map(int,input().split())
# watchhouse=[]
# for _ in range(neiborhood):
#     watchhouse.append(int(input()))
# houses,neiborhood,*watchhouse,=map(int,open(0).read().split())
# safe=unsafe=0
# k,z=watchhouse[0],watchhouse[-1]
# total=(houses*houses+houses)/2
# if k!=1:
#     if z!=houses:
#         watchhouse=[1,*watchhouse,houses]
#     else:
#         watchhouse=[1,*watchhouse]
# else:
#     if z!=houses:
#         watchhouse.append(houses)
# p=len(watchhouse)
# gap=[watchhouse[i+1]-watchhouse[i]-1 for i in range(p-1)]
# for i in range(p-1):
#     unsafe+=gap[i]*(gap[i]+1)/2
# print(f"saf {total}, unsaf {unsafe}")
# print(int(total-unsafe))


# houses,neiborhood=map(int,input().split())
# watchhouse=[]
# for _ in range(neiborhood):
#     watchhouse.append(int(input()))
# watchhouse={*watchhouse}
# safe=0
# for i in range(1,houses+1):
#     for j in range(houses,0,-1):
#         if watchhouse&{*range(i,j+1)}:
#             safe+=1
# print(safe)


houses,neiborhood=map(int,input().split())
watchhouse=[]
for _ in range(neiborhood):
    watchhouse.append(int(input()))
# houses,neiborhood,*watchhouse,=map(int,open(0).read().split())
safe=0
for i in range(1,houses+1):
    for j in range(houses,i-1,-1):
        for k in range(neiborhood):
            if i<=watchhouse[k]<=j:
                safe+=1
                break
print(safe)


