# integerlists.py
# Integer Lists

i,j=int,input;from collections import deque as d
def x(z,l,r=0):
 for c in z:
  if'R'==c:r^=1
  else:
   if not l:return"error"
   [l.pop()if r else l.popleft()]
 if r:l.reverse()
 return'['+','.join(map(str,l))+']'
exec("z,_=j(),j();l=j()[1:-1].split(',');l=d()if l==['']else d(map(i,l));print(x(z,l));"*i(j()))


# 1st attempt:
# i,j=int,input;from collections import deque as d
# def x(z,l):
#   r=0
#   for c in z:
#     if c=='R':r=r^1
#     else:
#       if not l:return"error"
#       if r:l.pop()
#       else:l.popleft()
#   if r:l.reverse()
#   return '[' + ','.join(map(str, l)) + ']'
# exec("z,_=j(),j();l=j()[1:-1].split(',');l=d()if l==['']else d(map(i,l));print(x(z,l));"*i(j()))


# original:
# from collections import deque
# def execute(cmd, lst):
#     reverse_flag=0
#     for c in cmd:
#         if c=='R':reverse_flag=not reverse_flag
#         else:
#             if not lst:return"error"
#             if reverse_flag:lst.pop()
#             else:lst.popleft()
#     if reverse_flag:lst.reverse()
#     return '[' + ','.join(map(str, lst)) + ']'
# exec("cmd,_=input(),input();lst=input()[1:-1].split(',');lst=deque()if lst==['']else deque(map(int,lst));print(execute(cmd, lst));"*int(input()))