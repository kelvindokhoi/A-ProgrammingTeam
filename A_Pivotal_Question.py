# A Pivotal Question
# https://open.kattis.com/contests/ue23kp/problems/apivotalquestion

m = 0

n,*array, = map(int,input().split())
dp_minright = [0]*(n)
dp_maxleft = [0]*(n)

for i in range(n):
    if i==0:
        dp_maxleft[0] = -float('inf')
        dp_minright[-1] = float('inf')
    else:
        dp_maxleft[i] = max(dp_maxleft[i-1],array[i-1])
        
        dp_minright[n-1-i] = min(dp_minright[n-i],array[n-i])

pivots = []
for i in range(n):
    if dp_minright[i]>=array[i]>=dp_maxleft[i]:
        m+=1
        if m<=100:
            pivots.append(array[i])

# print(array)
if m>0:
    print(m,*pivots)
else:
    print(0)
# print("minright: ", dp_minright)
# print("maxleft: ", dp_maxleft)