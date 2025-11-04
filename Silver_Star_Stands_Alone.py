# Silver Star Stands Alone
# https://open.kattis.com/problems/silverstarstandsalone

import math
P = int(input())
if P==2:
    print(1)
else:

    sieve = [0] * (P + 1)

    for i in range(2, int(math.sqrt(P)) + 1):
        if sieve[i] == 0:
            for j in range(i * 2, P + 1, i):
                sieve[j] = 1

    primes = [i for i in range(2, P + 1) if sieve[i] == 0]

    dp = [0]*len(primes)
    dp[0] = 1
    for i in range(1,len(primes)):
        number_of_ways = 0
        j = i-1
        while j>-1 and primes[i]-primes[j]<15:
            number_of_ways += dp[j]
            j-=1
        dp[i] = number_of_ways


    # print(select_a_number(primes,1,2))
    # print(primes)
    print(dp[-1])
    # print(dp)
