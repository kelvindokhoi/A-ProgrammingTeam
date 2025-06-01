# Transit_Woes.py

# transitwoes
# https://open.kattis.com/problems/transitwoes

# python Transit_Woes.py < Transit_Woes_in.txt


start,end,n = map(int,input().split())
walk_time = [*map(int,input().split())] #walk n+1 times
bus_time = [*map(int,input().split())] #ride the bus n times
bus_interval = [*map(int,input().split())] #the arriving intervals of buses
start += walk_time[0]
for i in range(n):
    start += (-start%bus_interval[i])+bus_time[i]+walk_time[i+1]
print('no'if start>end else'yes')

# golfed:
# a,w,v,k=[[*map(int,l.split())]for l in open(0)];h=a[0]+w[0]
# for x in range(a[2]):h+=-h%k[x]+v[x]+w[x+1]
# print(['yes','no'][h>a[1]])