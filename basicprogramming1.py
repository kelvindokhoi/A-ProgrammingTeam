# basicprogramming1

N,t,*m,=[*map(int,open(0).read().split())];i,k=m[:2]
def j():
 i,w=m[0],{0}
 while~-N!=i:
  if~-N<i:return"Out"
  if{i}&w:return"Cyclic"
  w.add(i);i=m[i]
 return"Done"
print([7,("Smaller","Equal","Bigger")[(i>=k)+(i>k)],sorted(m[:3])[1],sum(m),sum(s for s in m if~s&1),''.join(chr(x%26+97)for x in m),j()][~-t])