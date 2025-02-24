    # 11614 - Etruscan Warriors Never Play Chess
# from bisect import bisect_left

# create possible answers
# answers = [i*(i+1)>>2 for i in range(10**9)]

from math import sqrt,floor

for _ in range(int(input())):
    try: print(floor(sqrt(2*int(input())+0.25)-0.5))
    except ValueError:
        break

# int(sqrt(2*int(input())-0.25)-0.5)