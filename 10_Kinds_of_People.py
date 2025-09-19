# 10 Kinds of People
# https://open.kattis.com/contests/hd35qb/problems/10kindsofpeople

n,m = map(int,input().split())
the_map = [[int(i) for i in input()] for _ in range(n)]
floyd = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(int(input())):
    r1,c1,r2,c2 = map(int,input().split())
    if the_map[c2][r2] != the_map[c1][r1]:
        print("neither")
    
