# Bobby's Bet

import math

def binomial_probability(n, k, p):
    combi = math.comb(n, k)
    return combi * (p ** k) * ((1 - p) ** (n - k))
cases = int(input())
for _ in range(cases):
    R, S, X, Y, W = map(int, input().split())
    if R > S:
        print('no')
        continue
    p = (S - R + 1) / S
    win_probability = sum(binomial_probability(Y, k, p) for k in range(X, Y + 1))
    expected_return = win_probability * W
    if expected_return > 1:
        print('yes')
    else:
        print('no')