# Shortlex
# https://open.kattis.com/contests/ab9rhp/problems/shortlex
# python Shortlex.py < Shortlex_in.txt

nums = [int(input()) for _ in range(int(input()))]

cache = {0:'',1:'0',2:'1'}

for num in nums:
    output = ''
    if num==1:
        print(0)
        continue
    if num==2:
        print(1)
        continue
    while num not in cache:
        if num%2==1:
            num = (num-1)//2
            output = '0' + output
        else:
            num = (num-2)//2
            output = '1' + output
        if num in cache:
            output = cache[num] + output
            break
    print(output)
