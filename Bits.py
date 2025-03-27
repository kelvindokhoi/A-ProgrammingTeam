# Bits
# bits

for _ in' '*int(input()):
    num = input()
    global_max = 0
    for i in range(1,-~len(num)):
        local_max = 0
        curr = int(num[:i])
        while curr:
            local_max += curr&1
            curr >>= 1
        global_max = max(global_max,local_max)
    print(global_max)


# exec("c='';print(max(bin(int(c:=c+n)).count('1')for n in input()));"*int(input()))
