# 10209 - Is This Integration

# Monte-Carlo Approximation

# python 10209-Is_This_Integration.py < 10209-Is_This_Integration_in.txt > 10209-Is_This_Integration_out.txt
# from random import uniform
# from math import dist

# allnums = map(float,open(0).read().split())

# for num in allnums:
#     LDcorner = [0,0]
#     LUcorner = [0,num]
#     RDcorner = [num,0]
#     RUcorner = [num,num]
#     middle = 0
#     flower = 0
#     total = num**2
#     testcases = 10000000
#     for i in range(testcases):
#         new = [uniform(0,num),uniform(0,num)]
#         LD = dist(new,LDcorner)<=num
#         LU = dist(new,LUcorner)<=num
#         RD = dist(new,RDcorner)<=num
#         RU = dist(new,RUcorner)<=num
#         if LD and LU and RD and RU:
#             middle+=1
#         elif (LD and RU) or (LU and RD):
#             flower+=1
#     n1 = "{:0.3f}".format(middle/testcases*total)
#     n2 = "{:0.3f}".format(flower/testcases*total)
#     print(n1,n2,"{:0.3f}".format(total-float(n1)-float(n2)))

# Mathematic Approach
from math import sqrt,pi

allnums = map(float,open(0).read().split())
for num in allnums:
    Acorner = num*num*(1-sqrt(3)/4-pi/6)*4
    Aleaf = num*num*(sqrt(3)/2+pi/12-1)*4
    Amiddle = num*num-Acorner-Aleaf
    print(f"{Amiddle:0.3f} {Aleaf:0.3f} {Acorner:0.3f}")