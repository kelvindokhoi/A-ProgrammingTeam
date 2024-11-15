ii = int(input())

tter = {}
for i in range(ii):
    i, j = map(str, input().split(" "))
    j = eval(j)
    if i in tter:
        tter[i]=tter[i]+j
    else:
        tter[i]= j

tter = dict(sorted(tter.items(), key=lambda item: item[1], reverse=True))
print(next(iter(tter)))