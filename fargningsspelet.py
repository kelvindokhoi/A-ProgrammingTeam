# fargningsspelet.py
# The Coloring Game
def a(m):z[m]=z[(m+1)%n]=z[(m-1)%n]=1;print(m+1);m=int(input())-1;[m>-2 or exit()];z[m]=1;return m
n,_=map(int,input().split());z=[0]*n;z[(x:=~-int(input()))]=1
if n%2:a(-z[0]%n);[z[i]or a(i)for i in range(n)]
else:exec('x=a(n+~x);'*n)