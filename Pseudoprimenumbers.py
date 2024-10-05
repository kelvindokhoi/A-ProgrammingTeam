mod = 1

def fastExpo_combine_mod(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base % mod
    if exp % 2 == 0:
        return fastExpo_combine_mod(base*base % mod, exp//2)
    else:
        return fastExpo_combine_mod(base*base % mod, (exp-1)//2)*base%mod
    
def main():
    ans = []
    global mod
    remain = 0
    while True:
        mod, base = map(int, input().split(" "))
        if mod == 0 and base == 0:
            break
        remain = fastExpo_combine_mod(base, mod)
        print(remain)
        if remain == base:
            ans.append("yes")
        else:
            ans.append("no")
    for i in range(len(ans)):
        print(ans[i])

if __name__ == '__main__':
    main()