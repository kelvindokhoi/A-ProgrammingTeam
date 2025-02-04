# freckles.py
# Prim's Algorithm

import math;from heapq import*;o=lambda a,b:math.dist(a,b);j,k=input,heappush
for i in' '*int(j()):
 j();u=[tuple(map(float,j().split()))for _ in' '*int(j())];a,s,e=set([u.pop()]),0,[];[[k(e,(o(m,n),m))for n in a]for m in u]
 while u:
  w,v=heappop(e)
  if v in a:continue
  s+=w;a.add(v);u.remove(v);[x in a or k(e,(o(v,x),x))for x in u]
 print(f"{s:.2f}")


# Original
# from math import *
# import heapq
# weight = lambda x1,x2,y1,y2:sqrt((x1-y1)**2+(x2-y2)**2)
# for i in range(int(input())):
#     input()
#     untrvl = [tuple(map(float,input().split())) for _ in range(int(input()))]
#     passed = set([untrvl.pop()])
#     sum=0
#     edges=[]
#     for p1 in untrvl:
#         for p2 in passed:
#             heapq.heappush(edges,(weight(p1[0],p1[1],p2[0],p2[1]),p1))
#     while untrvl:
#         w,point = heapq.heappop(edges)
#         if point in passed:continue
#         sum+=w;passed.add(point);untrvl.remove(point)
#         for pt in untrvl:
#             pt in passed or heapq.heappush(edges, (weight(point[0], point[1], pt[0], pt[1]), pt))
#     print(f"{sum:.2f}")

# AI-optimized version (0.21s):
# import sys
# from array import array

# def calculate_mst():
#     T = int(sys.stdin.readline())
#     for _ in range(T):
#         sys.stdin.readline()
#         n = int(sys.stdin.readline())

#         x_coords = array('d', [0.0] * n)
#         y_coords = array('d', [0.0] * n)

#         for i in range(n):
#             x, y = sys.stdin.readline().split()
#             x_coords[i] = float(x)
#             y_coords[i] = float(y)

#         visited = [False] * n
#         min_dist_sq = [float('inf')] * n
#         min_dist_sq[0] = 0.0
#         total_weight = 0.0
#         edges_added = 0

#         while edges_added < n:
#             min_v = -1
#             min_w_sq = float('inf')

#             for v in range(n):
#                 if not visited[v] and min_dist_sq[v] < min_w_sq:
#                     min_w_sq = min_dist_sq[v]
#                     min_v = v

#             visited[min_v] = True
#             total_weight += min_w_sq**0.5
#             edges_added += 1

#             x1 = x_coords[min_v]
#             y1 = y_coords[min_v]

#             # Pre-calculate squares to avoid repeated calculations in the inner loop.
#             for v in range(n):
#                 if not visited[v]:
#                     dx = x1 - x_coords[v]
#                     dy = y1 - y_coords[v]
#                     dist_sq = dx * dx + dy * dy  # No sqrt here!
#                     min_dist_sq[v] = min(min_dist_sq[v], dist_sq)
#         print(f"{total_weight:.2f}")
# if __name__ == "__main__":
#     calculate_mst()


    
