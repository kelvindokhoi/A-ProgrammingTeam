# Bottled-Up Feelings
# bottledup

a,b,c=map(int,input().split())
def solve(a,b,c):
    limit_b = a//b
    limit_c = a//c
    solutions = []
    for i in range(limit_b+1):
        if (a-i*b)%c==0:
            j=(a-i*b)//c
            solutions.append((i+j,i,j))
    return solutions

solutions = solve(a,b,c)
if solutions:
    ans = sorted(solutions)[0]
    print(ans[1],ans[2])
else:
    print('Impossible')