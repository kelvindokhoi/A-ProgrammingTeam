def G(h):return{(x,h-1-y)for y in range(h)for x,c in enumerate(input())if c=='#'}
for _ in[0]*int(input()):
 w,h,s=map(int,input().split());S=[G(h),G(h)];t=d=0
 for _ in[0]*s:
  x,y=map(int,input().split())
  if d:continue
  if(x,y)in S[~t]:S[~t].discard((x,y));d=not S[~t]and t;t|=not S[~t]
  elif t and not S[t]:d=1
  else:t=~t
 print('draw'if all(S)or not any(S)else f"player %s wins"%('one'if S[0]else'two'))