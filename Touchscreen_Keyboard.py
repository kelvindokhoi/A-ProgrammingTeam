# Touchscreen_Keyboard.py

# touchscreenkeyboard
# https://open.kattis.com/problems/touchscreenkeyboard

# python Touchscreen_Keyboard.py < Touchscreen_Keyboard_in.txt

# typical touchscreen keyboard:
# qwertyuiop
# asdfghjkl
# zxcvbnm

import heapq

translate = dict()
translate.update(dict(zip('qwertyuiop',[(0,i)for i in range(len('qwertyuiop'))])))
translate.update(dict(zip('asdfghjkl',[(1,i)for i in range(len('asdfghjkl'))])))
translate.update(dict(zip('zxcvbnm',[(2,i)for i in range(len('zxcvbnm'))])))

def offset(c1:str,c2:str):
    c1_coor = translate[c1]
    c2_coor = translate[c2]
    return abs(c1_coor[0]-c2_coor[0])+abs(c1_coor[1]-c2_coor[1])

for _ in[0]*int(input()):
    original, case = input().split()
    all_words = []
    for _ in[0]*int(case):
        new = input()
        heapq.heappush(all_words,(sum(offset(i,j)for i,j in zip(original,new)),new))
    while all_words:
        sum_offset, word = heapq.heappop(all_words)
        print(word,sum_offset)
