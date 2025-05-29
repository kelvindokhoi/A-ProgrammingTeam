# WERTYU.py

# wertyu
# https://open.kattis.com/problems/wertyu

# python WERTYU.py < WERTYU_in.txt

dictionary = dict(zip(r" 1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./",r" `1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,."))
while 1:
    try:
        print((''.join(dictionary[c] for c in input())))
    except:break

import sys;t=r"1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./  "
for l in sys.stdin:print(''.join(dict(zip(t,'`'+t))[c]for c in l[:-1]))

# golfed:
# import sys;t=r"1234567890-=QWERTYUIOP[]\ASDFGHJKL;'ZXCVBNM,./  ";[print(''.join(dict(zip(t,'`'+t))[c]for c in l[:-1]))for l in sys.stdin]