# Above Average
# https://open.kattis.com/contests/jesw36/problems/aboveaverage
from bisect import bisect_right
for _ in range(int(input())):
    *grades, = map(int,input().split())
    n = grades.pop(0)
    grades.sort()
    avg = sum(grades)/n
    print(f"{100*(n-bisect_right(grades,avg))/n:0.3f}%")
