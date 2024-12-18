# provincesandgold
# Provinces and Gold

# g,s,c=map(int,input().split())
# P=g*3+s*2+c
# V="Province"if P>7 else"Duchy"if P>4 else"Estate"if P>1 else""
# T="Gold"if P>5 else"Silver"if P>2 else"Copper"
# print(V+" or "+T if V else T)

# i=int;k=input().split();p=i(k[0])*3+i(k[1])*2+i(k[2]);a=[0,6,11,19,25,31,36];v="EstateDuchyProvinceCopperSilverGold or ";print(v[19:25]if p<2 else v[a[i(p>4)+i(p>7)]:a[i(p>4)+i(p>7)+1]]+v[35:]+v[a[i(p>2)+i(p>5)+3]:a[i(p>2)+i(p>5)+4]])

# most concise:
g,s,c=map(int,input().split());P=g*3+s*2+c;V=(("Estate",""),("Duchy","Province"))[P>4][P>7];T=(("Copper",""),("Silver","Gold"))[P>2][5<P];print(T if P<2 else V+" or "+T)

# exec(bytes('Ⱨⱳ㵣慭⡰湩ⱴ湩異⡴⸩灳楬⡴⤩倊朽㌪猫㈪挫嘊⠽∨獅慴整Ⱒ∢Ⱙ∨畄档≹∬牐癯湩散⤢嬩㹐崴偛㜾੝㵔⠨䌢灯数≲∬⤢⠬匢汩敶≲∬潇摬⤢嬩㹐崲㕛值੝牰湩⡴⁔晩倠㈼攠獬⁥⭖•牯∠含 ','u16')[2:])