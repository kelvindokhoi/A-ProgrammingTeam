# exactchange.py
# Exact Change
n = int(input())
bills = [0,0,0,0,0]
available_bills = [150,30,15,5,1]
i=0
while n!=0:
    if n<available_bills[i]:
        i += 1
    else:
        bills[i]+=1
        n -= available_bills[i]
print(' '.join(str(x) for x in bills[::-1]))