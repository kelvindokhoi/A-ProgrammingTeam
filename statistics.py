# # statistics
# # Statistics

# k=0
# while 1:
#     try:
#         k+=1
#         a=[*set(list(input().split())[1:])]
#         a.sort(key= lambda x: int(x))
#         print(f"Case {k}:",a[0],a[-1],int(a[-1])-int(a[0]))
#     except:break


# k=0
# while 1:
#  try:k+=1;a=sorted({int(x)for x in input().split()[1:]});print(f"Case {k}:",m:=a[0],n:=a[-1],n-m)
#  except:break

k=0
while 1:
 try:k+=1;a=map(int,input().split()[1:]).sort();print(f"Case {k}:",m:=a[0],n:=a[-1],n-m)
 except:break
 