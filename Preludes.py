# Preludes.py

# chopin
# https://open.kattis.com/problems/chopin

# python Preludes.py < Preludes_in.txt

import sys

for num,l in enumerate(sys.stdin):
    if 'b'in l:
        #Alternate
        if l[0]>'A':
            new_chord = chr(ord(l[0])-1)+'#'+l[2:-1]
        else:new_chord = 'G#'+l[2:-1]
    elif '#' in l:
        if l[0]<'G':
            new_chord = chr(ord(l[0])+1)+'b'+l[2:-1]
        else:new_chord = 'Ab'+l[2:-1]
    else:new_chord = 'UNIQUE'
    print(f'Case {num+1}: {new_chord}')

# golfed:
# for i,x in enumerate(__import__('sys').stdin):o=ord(x[0])-65;print('Case %d: %s'%(i+1,"GABCDEF"[o]+"#"+x[2:-1]if"b"in x else"BCDEFGA"[o]+"b"+x[2:-1]if"#"in x else"UNIQUE"))