# Rice judge

# https://open.kattis.com/problems/risdomare

num = int(input())

command = input()

rice_paddy = [(i,*map(int,input().split()))for i in range(1,num+1)] #num,size

if command[0]=='a': #>portion
    rice_paddy.sort(key=lambda x:(x[1]+x[2],x[1],x[2]),reverse=True)
else:
    rice_paddy.sort(key=lambda x:(x[1]+x[2],x[2],x[1]),reverse=True)
# print(rice_paddy)
print(rice_paddy[0][0])


