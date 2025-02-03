def do(i):
    U[i] = U[(i+1)%N] = U[(i-1)%N] = 1;print(f'curr map: {U}'); print(i+1); s = int(input())-1
    if s == -2: exit(0)
    U[s] = 1; return s
N, _ = map(int, input().split()); U = [0]*N
s = int(input())-1; U[s] = 1
print(f'curr map: {U}')
if N%2 == 0:
    while True: s=do(N-1-s)
else:
    do(-U[0]%N)
    for i in range(N):
        print(i)
        U[i] or do(i)
        print(U)