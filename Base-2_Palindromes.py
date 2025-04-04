# Base-2 Palindrome


import math

num = int(input())
n = math.floor(math.log2(num))


if num-(1<<(n)) < 1<<(n-1):
    pattern = [*bin(n)[2:]]
    text = ['1']*(n*2-1)
    text[0:len(pattern)] = pattern[::1]
    text[n*2-1-len(pattern):n*2] = pattern
    print(int("".join(text),2))
else:
    pattern = [*bin(n)[2:]]
    text = ['1']*(n*2)
    text[0:len(pattern)] = pattern[::1]
    text[n*2-len(pattern):n*2+1] = pattern
    print(int("".join(text),2))

