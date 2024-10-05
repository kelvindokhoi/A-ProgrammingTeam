arr = [0]*10

existedMod = []

for i in range(10):
    arr[i] = int(input())

for i in range(10):
    if not(arr[i]%42 in existedMod):
        existedMod.append(arr[i]%42)

print(len(existedMod))