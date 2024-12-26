# stararrangements

# a=int(input())
# l=(a+1)//2+1
# print(f"{a}:")
# for x in range(2,l):
#     for y in range(1,x+1):
#         if (x==y or x==y+1) and (a%(x+y)==0 or (a+y)%(x+y)==0):
#             print(f"{x},{y}")

# a=int(input());print(f"{a}:");[(lambda x,y:print(f"{x},{y}"))(x,y) for x in range(2,(a+3)//2) for y in range(1,x+1) if (x==y or x==y+1) and (a%(x+y)==0 or (a+y)%(x+y)==0)]
# a=int(input());print(f"{a}:");[print(f"{x},{y}") for x in range(2,(a+3)//2) for y in range(1,x+1) if (x==y or x==y+1) and (a%(x+y)==0 or (a+y)%(x+y)==0)]
# a=int(input());print(f"{a}:");[print(f"{x},{y}")for x in range(2,(a+3)//2)for y in range(1,x+1)if(x in[y,y+1])and(a%(x+y)==0 or(a+y)%(x+y)==0)]
# a=int(input());print(f"{a}:");[print(f"{x},{y}")for x in range(2,(a+3)//2)for y in range(1,x+1)if x in[y,y+1]and(a%(x+y)<1 or(a+y)%(x+y)<1)]
# a=int(input());print(f"{a}:");[print(f"{x},{y}")for x in range(2,(a+3)//2)for y in range(max(1,x-1),x+1)if(a%(x+y)<1 or(a+y)%(x+y)<1)]
a=int(input());print(f"{a}:");[print(f"{x},{y}")for x in range(2,(a+3)//2)for y in[x-1,x]if y>0 and(a%(x+y)<1 or(a+y)%(x+y)<1)]