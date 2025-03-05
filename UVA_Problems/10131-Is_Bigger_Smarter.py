# 10131
# Is Bigger Smarter?


# *f,=map(int,open('10131_sample_in.txt').read().split()) #Debugging line, the code starts from below
import sys
f = sys.stdin.read().split()
def keyE(elephant):return elephant['weight']*1e6+elephant['iq']
n = len(f) // 2
elehehe = [{'name': i + 1, 'weight': int(f[2 * i]), "iq":int(f[2 * i + 1])} for i in range(n)]
elehehe.sort(key=keyE)
DynamicElephants = [1]*n
TroopOfElephants = [[]for _ in range(n)]
best = []
max_len = 1
for i in range(n-1,-1,-1):
    TroopOfElephants[i]=[elehehe[i]['name']]
    for j in range(i+1,n):
        if elehehe[i]['iq']>elehehe[j]['iq']:
            if DynamicElephants[j]+1>DynamicElephants[i]:
                DynamicElephants[i]=DynamicElephants[j]+1
                TroopOfElephants[i]=[elehehe[i]['name']]+TroopOfElephants[j]
            if DynamicElephants[i]>max_len:
                max_len=DynamicElephants[i]
                best = TroopOfElephants[i]
print(max_len)
print(*best,sep="\n")