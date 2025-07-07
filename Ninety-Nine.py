# Ninety-Nine.py

# https://open.kattis.com/problems/ninetynine

print(1)
total = 1
while total!=99:
    op = int(input())
    if (op+1)%3==0:
        choice = op+1
    else:
        choice = op+2
    total = choice
    print(total)