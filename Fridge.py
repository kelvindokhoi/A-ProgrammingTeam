# Fridge

from collections import Counter

my_str = input()

pivot = [int(x) for x in '1234567890']

number = [0]*10
for char in my_str:
    if char=='0':
        number[0]+=1
    else:
        number[int(char)-1]+=1
max_n = 0
min_n = 0
for i in pivot:
    if number[i]>=max_n:
        max = number[i]
    else:
        min_n = min(number[:pivot.index(i)])