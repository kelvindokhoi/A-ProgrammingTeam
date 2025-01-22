# # basicprogramming2
# # Basic Programming 2



N,t,*A,=map(int,open(0).read().split())
if t==1:S=set(A);print(["No","Yes"][any(7777-x in S for x in S)])
if t==2:print(["Contains duplicate","Unique"][len(A)==len({*A})])
if t==3:from collections import Counter;c=Counter(A);r=[k for k,v in c.items()if v>N/2];print(' '.join(map(str,r))if len(r)else -1)
if t==4:A.sort();m=N//2;print([f"{A[m-1]} {A[m]}",A[m]][N%2])
if t==5:print(*sorted(x for x in A if 99<x<1000))


# N,t,*A,=map(int,open(0).read().split())
# if t==1:S=set(A);print(["No","Yes"][any(7777-x in S for x in S)])
# elif t==2:print(["Contains duplicate","Unique"][len(A)==len({*A})])
# elif t==3:from collections import Counter;c=Counter(A);r=[k for k,v in c.items()if v>N/2];print(' '.join(map(str,r))if len(r)else -1)
# elif t==4:A.sort();m=N//2;print([f"{A[m-1]} {A[m]}",A[m]][N%2])
# elif t==5:print(*sorted(x for x in A if 99<x<1000))

# N,t=map(int,input().split())
# A=list(map(int,input().split()))
# if t==1:S=set(A);print("Yes"if any(7777-x in S for x in S)else"No")
# elif t==2:print("Unique"if len(A)==len(set(A))else"Contains duplicate")
# elif t==3:from collections import Counter;c=Counter(A);r=[k for k,v in c.items()if v>N/2];print(' '.join(map(str,r))if len(r)else -1)
# elif t==4:A.sort();m=N//2;print(A[m]if N%2 else f"{A[m-1]} {A[m]}")
# elif t==5:print(*sorted(x for x in A if 99<x<1000))




# Key optimizations:

# For task 1 (finding pair sum 7777):
# Used set for O(1) lookups
# Added x!=7777-x check to handle edge cases
# Removed separate function call overhead
# For task 2 (checking uniqueness):
# Direct length comparison of list vs set
# Removed list conversion overhead
# For task 3 (finding majority element):
# Used Counter for efficient counting
# Single list comprehension
# Used unpacking for clean output
# For task 4 (finding median):
# Single sort operation
# Direct indexing
# f-string for cleaner output
# For task 5 (numbers between 100 and 999):
# Combined sorting and filtering in one step
# Used unpacking for output
# Simplified bounds checking
# General optimizations:
# Removed unnecessary functions
# Used elif chain
# Minimized variable creation
# Used list comprehension where beneficial
# Removed redundant type conversions



# from bisect import bisect_left,bisect_right
# N,t=map(int,input().split())
# Nmap=[*map(int,input().split())]
# def f():
#  if any(7777-x in Nmap for x in Nmap):return "Yes"
#  return "No"
# if t==1:print(f()) #checked
# if t==2:
#  print("Unique"if Nmap==[*{*Nmap}]else"Contains duplicate")
# def g():
#  a=[str(x) for x in{*Nmap}if Nmap.count(x)>N/2]
#  if len(a)==0:return -1
#  return " ".join(a)
# def h():
#  b=sorted(Nmap)
#  if N%2==1:
#   return b[N//2]
#  else:return str(b[N//2-1])+' '+str(b[N//2])
# def j():
#  b=sorted(Nmap)
#  m,n=bisect_right(Nmap,101)+1,bisect_left(Nmap,998)-1
#  return " ".join([str(x)for x in b[m:n]])

# if t==3:print(g())
# if t==4:print(h())
# if t==5:print(j())