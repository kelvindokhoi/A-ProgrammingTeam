# Alien Math
# https://open.kattis.com/contests/c7gven/problems/alienmath
import re
num_digit = int(input())
digits = input().split()
convert = dict(zip(digits,range(len(digits))))
pattern = '('+'|'.join(f'(?:{digit})' for digit in digits)+')'
numstring = input()
allnums = re.findall(pattern,numstring)
summ = 0
counter = 0
for num in allnums[::-1]:
    summ+=convert[num]*(num_digit**counter)
    counter+=1
print(summ)