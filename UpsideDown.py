# Upside Down
# https://open.kattis.com/problems/upsidedown
input()
print(' '.join(sorted([x[::-1]for x in input().split()])[::-1]))
