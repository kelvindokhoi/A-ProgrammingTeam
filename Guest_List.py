# Guest List

# https://open.kattis.com/problems/gestalisti
guest = set()
for i in range(int(input())):
    op,g = input().split()
    if op=='+':
        guest.add(g)
    elif op=='-':
        guest.remove(g)
    else:
        print("Jebb"if g in guest else"Neibb")
