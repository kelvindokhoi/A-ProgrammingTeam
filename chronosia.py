# chronosia
# python chronosia.py < chronosia_in.txt > chronosia_out.txt && fc chronosia_out.txt chronosia_sample_out.txt

# from time import time

testcases = int(input())
def calc():
    n,m = map(int,input().split())  #n is num town, m is num path
    adjacency_list = {i:set() for i in range(1,n+1)}
    for _ in range(m):
        u,v = map(int,input().split())
        adjacency_list[u].add(v)
    found = 0
    for i in range(1,n+1):
        addlist = set()
        for j in adjacency_list[i]:
            for k in adjacency_list[j]:
                if i==k:
                    return 1
                addlist.add(k)
        adjacency_list[i].update(addlist)
    return 0
for _ in range(testcases):
    # start = time()
    print('YES'if calc() else'NO')
    # end = time()
    # print(f"Total elapsed time: {end-start}")
