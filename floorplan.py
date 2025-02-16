# floorplan.py

from math import sqrt
n=int(input())
divs=set()
alter=set()
for i in range(1,int(sqrt(n))+2):
    if n%i==0:
        divs.add(i)
for d in divs:
    alter.add(n//d)
for d in alter:
    divs.add(d)
for num1 in divs:
    for num2 in divs:
        if num1*num2==n:
            a=num1+num2
            b = num2-num1 if num2>num1 else num1-num2
            if a%2==0 and b%2==0:
                print(a//2,b//2)
                exit()
print('impossible')


# from bisect import bisect_left
# nums=[i**2 for i in range(100010)]
# def findval(m2,lo,hi):
#     if lo>=hi:
#         return -1
#     mid=(hi+lo)//2
#     mid2=nums[mid]
#     if m2-mid2==n:
#         return mid
#     if mid2<m2-n:
#         return findval(m2,mid+1,hi)
#     else:
#         return findval(m2,lo,mid-1)

# n=int(input())
# for m in range(bisect_left(nums,n**2)):
#     m2 = nums[m]
#     p=findval(m2,1,m+1)
#     if p!=-1:
#         print(m,p)
#         break
# if p==-1:
#     print('impossible')
