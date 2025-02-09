# outofsorts.py
# Out of Sorts

n,m,a,c,x=map(int,input().split());q=[(a*x+c)%m]
for i in range(~-n):q+=[(a*q[i]+c)%m]
def A(v,l=0,h=~-n):
 while(l<=h)and(z:=q[m:=(l+h)>>1])-v:(h:=~-m)if(z>v)else(l:=-~m)
 return[0,1][z==v]
print(sum(A(w)for w in q))

# 3rd attempt:
# n,m,a,c,x0=map(int,input().split());q=[(a*x0+c)%m]*(n)
# for i in range(n-1):q[i+1]=(a*q[i]+c)%m
# def A(v,l=0,h=n-1):
#  while l<=h and (z:=q[m:=(l+h)>>1])-v:(h:=m-1)if z>v else(l:=m+1)
#  return [0,1][z==v]
# print(sum(A(w)for w in q))

# 2nd attempt:
# n,m,a,c,x0=map(int,input().split());q=[(a*x0+c)%m]*(n)
# for i in range(n-1):q[i+1]=(a*q[i]+c)%m
# def A(v,l=0,h=n-1):
#  while l<=h:
#   if(z:=q[m:=(l+h)>>1])==v:return 1
#   [(h:=m-1)if z>v else(l:=m+1)]
#  return 0
# print(sum(A(w)for w in q))

# 1st attempt:
# n,m,a,c,x0=map(int,input().split());nums=[(a*x0+c)%m]+[0]*(n-1)
# for i in range(n-1):nums[i+1]=(a*nums[i]+c)%m
# def Ann(v,l=0,h=n-1):
#     while l<=h:
#         if(z:=nums[m:=(l+h)>>1])==v:return 1
#         [(h:=m-1)if z>v else(l:=m+1)]
#     return 0
# print(sum(Ann(num)for num in nums))

# Original:
# n,m,a,c,x0=map(int,input().split())
# nums=[0]*(n)
# nums[0]=(a*x0+c)%m
# for i in range(n-1):
#     nums[i+1]=(a*nums[i]+c)%m
# def Ann(var,lo=0,hi=n-1):
#     while lo<=hi:
#         mid=(lo+hi)//2
#         if nums[mid]==var:return True
#         if nums[mid]>var:hi=mid-1
#         else:lo=mid+1
#     return False
# occr=0
# for num in set(nums):
#     if Ann(num):
#         occr+=1
# print(occr)