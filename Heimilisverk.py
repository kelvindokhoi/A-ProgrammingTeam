# Heimilisverk

# https://open.kattis.com/problems/heimilisverk

tracking = set()
names = []
for i in range(int(input())):
    I = input()
    if I not in tracking:
        names.append(I)
        tracking.add(I)

for name in names:
    print(name)