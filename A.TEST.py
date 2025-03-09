M,R,G,H,P=max,range,int,input,print
for _ in' '*G(H()):
 n,m=G(H()),[*map(G,H().split())];h=-~sum(m);d,c=[1e3]*h*-~n,['']*h*-~n;d[0]=0
 for i in R(1,-~n):
  for j in R(h):
   O,v,I=i*h+j,m[~-i],h*~-i+j
   if(w:=M(d[I-v],j))<d[O]:d[O],c[O]=w,c[I-v]+'U'
   if j+v<h and(q:=M(d[I+v],j+v))<d[O]:d[O],c[O]=q,c[I+v]+'D'
 print(c[n*h]if d[n*h]-1e3 else'IMPOSSIBLE')