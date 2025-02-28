# 10935 - Throwing cards away I


# Solution 1:
from queue import Queue
while(n:=int(input()))!=0:
    a = Queue()
    ans=[]
    for i in range(1, n + 1):
        a.put(i)
    while a.qsize()>1:
        ans.append(a.get())
        a.put(a.get())
    print('Discarded cards:',end='')
    if ans:
        print(' ',end='')
        print(*ans,sep=', ')
    else:print()
    print(f'Remaining card: {a.get()}')