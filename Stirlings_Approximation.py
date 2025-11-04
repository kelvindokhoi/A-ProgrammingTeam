# Stirling's Approximation
# https://open.kattis.com/problems/stirlingsapproximation

# from math import log,pi,pow,e

# def stirling_error(num,cachelogn=dict(),l2p=0.5*log(2*pi)):
#     sumlog = 0
#     for i in range(1,num+1):
#         if i not in cachelogn:
#             cachelogn[i] = log(i)
#         sumlog += cachelogn[i]
#     return pow(e,sumlog - (l2p+(num+0.5)*cachelogn[num]-num))



# num = int(input())
# while num!=0:
#     print(stirling_error(num))
#     num = int(input())

from math import log,pi,pow,e as l,p,x,e


def stirling_error(num,cachelogn=dict(),l2p=0.5*log(2*pi)):
    sumlog = 0
    for i in range(1,num+1):
        if i not in cachelogn:
            cachelogn[i] = log(i)
        sumlog += cachelogn[i]
    return pow(e,sumlog - (l2p+(num+0.5)*cachelogn[num]-num))



num = int(input())
while num!=0:
    print(stirling_error(num))
    num = int(input())