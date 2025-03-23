
# python Running_MoM.py < Running_MoM_in.txt

flights = int(input())
nameconvert = dict()
adjacency_list = dict()
i=0
for _ in range(flights):
    go_in, go_out = input().split()
    if go_in not in nameconvert:
        nameconvert[go_in]=i
        i+=1
    if go_out not in nameconvert:
        nameconvert[go_out]=i
        i+=1
    if go_in in adjacency_list:
        adjacency_list[go_in].add(go_out)
    else:
        adjacency_list[go_in]={go_out}
    if go_out not in adjacency_list:
        adjacency_list[go_out] = set()
total_name = len(nameconvert)
go_to_map = [[0 for i in ' '*total_name]for j in ' '*total_name]
# print(adjacency_list)
for i in adjacency_list.keys():
    for j in adjacency_list[i]:
        go_to_map[nameconvert[i]][nameconvert[j]]=1
for i in range(total_name):
    for j in range(total_name):
        for k in range(total_name):
            if go_to_map[i][j]==1 and go_to_map[j][k]==1: 
                go_to_map[i][k]=1

# print(adjacency_list)
safe = set()
for i in range(total_name):
    if go_to_map[i][i]==1:
        safe.add(i)
updated = set()
for i in range(total_name):
    for j in safe:
        if go_to_map[i][j]==1:
            updated.add(i)
safe.update(updated)
# print(safe)
# print(safe)
while True:
    try:
        name = input()
        if nameconvert[name] in safe:
            print(f"{name} safe")
        else:print(f"{name} trapped")
    except EOFError:exit()
