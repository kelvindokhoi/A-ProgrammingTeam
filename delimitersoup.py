# delimitersoup.py
# Delimiter Soup

s,p,i=[],print,0;input()
for _ in input():
 if _ in'{([':s+=[_]
 elif(' '!=_)*(not s or'{(['['})]'.find(_)]!=s.pop()):p(_,i);exit()
 i+=1
p('ok so far')


# exec(bytes('ⱳⱰ㵩嵛瀬楲瑮〬椻灮瑵⤨昊牯张椠⁮湩異⡴㨩 晩张椠❮⡻❛猺㴫彛੝攠楬❦✠㴡㩟 椠⁦潮⁴⁳牯笧嬨嬧紧崩⸧楦摮弨崩㴡⹳潰⡰㨩⡰ⱟ⥩攻楸⡴਩椠㴫਱⡰漧⁫潳映牡⤧','u16')[2:])

# from collections import*;s,i,p,e=deque(),input,print,exit;i()
# for i,_ in enumerate(i()):
#  if _ in'{([':s.append(_)
#  elif _!=' ':
#   if not s:p(_,i);e()
#   if'{(['['})]'.find(_)]!=s.pop():p(_,i);e()
# p('ok so far')
