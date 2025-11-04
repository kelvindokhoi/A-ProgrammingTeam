# Weightlifting
# https://open.kattis.com/contests/ab9rhp/problems/weightlifting

from mpmath import mpf, mp

mp.dps = 50

def compute_d(e, cs, cf):
  if e == 0:
    return mpf(225)

  g = [mpf(0) for _ in range(e + 1)]
  g[0] = mpf(1)

  for i in range(1, e + 1):
    val1 = g[i - cs] if i >= cs else mpf(1)
    val2 = g[i - cf] if i >= cf else mpf(1)
    g[i] = val1 + val2

  g_cf = g[e - cf] if e >= cf else mpf(1)

  numer = mpf(25) * g_cf + mpf(200)
  denom = g[e]

  d = numer / denom

  return d

import sys

e,cs,cf = map(int,input().split())
d = compute_d(e, cs, cf)

print(f"{float(d):.6f}")

