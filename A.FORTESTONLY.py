c=[9,4,4,4,7];F=C=0;import sys
for l in sys.stdin:
 if l[0]!="-":
  s=l.split();t=p=0
  for i,x in enumerate(s):
   n,u=int(x[:-1]),x[-1]
   if u=="%":p+=n/100
   else:t+=(n:=[n*c[i],n][u=='C'])
   if i==0:f,s=n,u
  t/=1-p;F+=f*[1,t/100][s=='%'];C+=t
 elif C:print(f"{F/C*100:.0f}%");F=C=0