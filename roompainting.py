# roompainting.py
# Room Painting

from bisect import*;i,j,*a=map(int,open(0).read().split());c=sorted(a[:i]);print(sum(c[bisect_left(c,x)]-x for x in a[i:]))

# Golfed 1st attempt:
# from bisect import*;n,m=map(int,input().split());c,p=sorted([int(input())for _ in' '*n]),[int(input())for _ in' '*m];print(sum(c[bisect_left(c,x)]-x for x in p))

# Original:
# from bisect import bisect_left

# n, m = map(int, input().split())
# cansize = sorted([int(input()) for _ in' '*n])
# paints = [int(input())for _ in' '*m]
# total_sum = 0
# for paint in paints:
#     suitable = bisect_left(cansize,paint)
#     total_sum+=cansize[suitable]-paint
# print(total_sum)

