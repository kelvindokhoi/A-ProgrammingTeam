# we have three colors: blue, red, green
# we have 6 faces need to be painted

def check(a,b):
    if a.count('r')==b.count('r') and a.count('b')==b.count('b'):
        a=[*a]
        combinations=[a]
        for i in range(4):
            a[0],a[1],a[5],a[4]=a[4],a[0],a[1],a[5]
            combinations+=["".join(a)]
            for i in range(4):
                a[2],a[1],a[3],a[4]=a[4],a[2],a[1],a[3]
                combinations+=["".join(a)]
                for i in range(4):
                    a[0],a[2],a[5],a[3]=a[3],a[0],a[2],a[5]
                    combinations+=["".join(a)]
        # print(combinations)
        if b in combinations:return "TRUE"
        else:return'FALSE'    
    else:
        return'FALSE'
    
while True:
    try:
        n=input()
        a,b=n[:6],n[6:]
        # print(a,b)
        print(check(a,b))
    except:break

# n=open(0).read().split()
# for i in range(len(n)):
#     a,b=n[i][:6],n[i][6:]
#     a,b=[*a],[*b]
#     print(check(a,b))