# throwns.py
# Game of Throwns


a,u,n,k=[],0,int(input()[:2]),0
for c in input().split():
 if c>'t'or u:u=exec('a.pop();'*int(c))if u else 1
 else:a+=[k+int(c)]
 k=a[-1]if a else 0
print(k%n)

# a,u=[],0;n=int(input().split()[0])
# for c in input().split():
#  if c!='undo'and not u:a+=[((a[-1]if a else 0)+int(c))%n]
#  else:u=exec('a.pop();'*int(c)+'u=0')if u else 1
# print(a[-1]if a else 0)

# a,u=[],False;n=int(input().split()[0])
# for c in input().split():
#     if u:exec('a.pop();'*int(c)+'u=False')
#     else:
#         if c!='undo':a+=[((a[-1]if a else 0)+int(c))%n]
#         else:u=True
# print(a[-1]if a else 0)

# actions,undo=[],False
# n=int(input().split()[0])
# for cmd in input().split():
#     if undo:exec('actions.pop();'*int(cmd));undo=False
#     else:
#         if cmd=='undo':undo=True
#         else:actions+=[((actions[-1]if actions else 0)+int(cmd))%n]
# print(actions[-1]if actions else 0)

