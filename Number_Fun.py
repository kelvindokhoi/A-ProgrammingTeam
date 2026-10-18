# Number Fun

def f(a,b,c):
    if a-b==c or b-a==c or a-c==b or c-a==b or b-c==a or c-b==a:
        return "Possible"
    if a*b==c or b*a==c or a*c==b or c*a==b or b*c==a or c*b==a:
        return "Possible"
    return "Impossible"

n_case = int(input())
for _ in range(n_case):
    a,b,c = map(int,input().split())
    print(f(a,b,c))
