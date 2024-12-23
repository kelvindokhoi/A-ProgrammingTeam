# oddgnome
# n=int(input())
# for i in range(n):
#     x=[*map(int,input().split())]
#     start=x[1]
#     j=1
#     for i in range(start,x[0]+start):
#         if x[j]!=i:
#             print(j)
#             break
#         j+=1

# for _ in[0]*int(input()):x=[*map(int,input().split())];s=x[1];print(next(j for j,v in enumerate(x[1:],1)if v!=s+j-1))

# shortest
# for _ in' '*int(input()):l=[*map(int,input().split())];print([i for i in range(1,l[0]+1)if l[i]!=l[1]+i-1][0])

# for _ in[0]*int(input()):a=[*map(int,input().split())];print(next(i for i in range(1,len(a))if a[i]!=a[1]+i-1))

# exec('l=[*map(int,input().split())];print([i for i in range(1,-~l[0])if-~l[i]!=l[1]+i][0]);'*int(input()))

exec('a,*l=map(int,input().split());print([i+1 for i in range(1,a)if l[i]!=l[0]+i][0]);'*int(input()))  


# exec(bytes('㵬⩛慭⡰湩ⱴ湩異⡴⸩灳楬⡴⤩㭝牰湩⡴楛映牯椠椠⁮慲杮⡥ⰱ縭孬崰椩ⵦ汾楛⅝氽ㅛ⭝嵩せ⥝※','u16')[2:]*int(input()))

# exec("l=[*map(int,input().split())];print(next(i for i in range(1,l[0]+1)if l[i]!=l[1]+i-1));"*int(input()))
