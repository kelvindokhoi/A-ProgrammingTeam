mod = 1000000007

def hate9(num):
    return 8*fastExpo_combine_mod(9,num-1)%mod

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
    answer = []
    n = int(input())
    for i in range(n):
        answer.append(hate9(int(input())))
    for i in range(n):
        print(answer[i])

if __name__ == '__main__':
    main()