# Longest Increasing Subsequence
# https://open.kattis.com/contests/oaojv8/problems/longincsubseq

from bisect import bisect_right

while True:
    try:
        length = int(input())
        *sequence, = map(int,input().split())
    except:
        break
    lis = []
    parent = {x:-1 for x in sequence}
    for i,num in enumerate(sequence):
        pos = bisect_right(lis,num)
        # print(pos,lis,index)
        if pos==len(lis):
            if len(lis)==0:
                lis.append(num)
                parent[num] = lis[pos-1]
            elif lis[pos-1]!=num:
                lis.append(num)
                parent[i] = lis[pos-1]
            else:
                lis[pos-1]=num
                index[pos-1] = i
                parent[i] = lis[pos-1]
        else:
            if lis[pos]>num and lis[pos-1]<num and pos==len(lis)-1:
                lis[pos]=num
                index[pos] = i
    if len(lis)!=0:
        print(len(lis))
        # print(lis)
        # print(index)
        print(" ".join(str(x) for x in index))
    else:
        print(0)
        print()
