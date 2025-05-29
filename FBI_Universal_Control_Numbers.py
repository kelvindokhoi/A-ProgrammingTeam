# FBI_Universal_Control_Numbers.py

# fbiuniversal
# https://open.kattis.com/problems/fbiuniversal

# python FBI_Universal_Control_Numbers.py < FBI_Universal_Control_Numbers_in.txt

ex = dict(zip('0123456789ACDEFHJKLMNPRTVWX',range(27)))
for _ in[0]*int(input()):
    index,serial = input().split()
    serial,check = serial[:-1],serial[-1]
    base = 1
    value = 0
    integer_value = 0
    for i in range(8):
        base += 2 if i&1 else 1
        value += base*ex[serial[i]]
        integer_value += ex[serial[i]]*(27**(7-i))
    if value % 27 == ex[check]:
        print(index,integer_value)
    else:
        print(index,'Invalid')

# golfed:
# e={x:i for i,x in enumerate('0123456789ACDEFHJKLMNPRTVWX')}
# for _ in[0]*int(input()):
#  I,S=input().split();s,c=S[:-1],S[-1];b=1;v=0;n=0
#  for i in range(8):
#   b+=2 if i&1 else 1;v+=b*e[s[i]];n+=e[s[i]]*27**(7-i)
#  print(I,n if v%27==e[c]else'Invalid')