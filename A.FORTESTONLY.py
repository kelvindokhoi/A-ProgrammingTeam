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