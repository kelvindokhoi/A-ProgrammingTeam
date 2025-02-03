# sort

from collections import*;print(*sum(([x]*y for x,y in sorted(Counter(open(0).read().split()[2:]).items(),key=lambda x:-x[1])),[]))

# from collections import*;print(*sum(([x]*y for x,y in sorted(Counter([*map(int,open(0).read().split())][2:]).items(),key=lambda x:-x[1])),[]))

# from collections import*
# print(*sum(([x]*y for x,y in sorted(Counter(list(map(int,open(0).read().split()))[2:]).items(),key=lambda x:-x[1])),[]))

# from collections import*
# _,m,*n=map(int,open(0).read().split())
# w=defaultdict(int)
# for k in n:w[k]+=1
# for x,y in sorted(w.items(),key=lambda x:x[1],reverse=True):
#     for _ in range(y):print(x,end=" ")

# from collections import defaultdict
# _,m=map(int,input().split())
# *n,=map(int,input().split())
# w=defaultdict(int)
# for k in n:
#     w[k]+=1
# for x,y in sorted(w.items(),key=lambda x:x[1],reverse=True):
#     for _ in range(y):
#         print(x,end=" ")
