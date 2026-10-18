
# python Running_MoM.py < Running_MoM_in.txt

def floydWarshall(dist):
    V = len(dist)
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if(dist[i][k] != float("inf") and dist[k][j]!= float("inf")):
                    dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])

num_flights = int(input())
num_to_f = dict()
f_to_num = dict()
starter = 0
total = []
for i in range(num_flights):
    start, end = input().split()
    if start not in f_to_num:
        f_to_num[start]=starter
        num_to_f[starter] = start
        starter+=1
    if end not in f_to_num:
        f_to_num[end]=starter
        num_to_f[starter]=end
        starter+=1
    total.append([f_to_num[start],f_to_num[end]])
num_pairs = len(num_to_f)
dist = [[float("inf") for _ in' '*num_pairs]for _ in ' '*num_pairs]
for i in range(num_pairs):
    dist[i][i]=float("inf")
for start,end in total:
    dist[start][end] = 1
floydWarshall(dist)
# for i in range(len(dist)):
#     for j in range(len(dist)):
#         print(dist[i][j], end=" ")
#     print()


for i in range(num_pairs):
    is_safe = False
    for j in range(num_pairs):
        if dist[j][j] < float("inf") and (dist[i][j] < float("inf") or i == j):
            is_safe = True
            break
    status = "safe" if is_safe else "trapped"
    f_to_num[num_to_f[i]]=status

while True:
    try:
        city = input()
        print(city,f_to_num[city])
    except:
        break
