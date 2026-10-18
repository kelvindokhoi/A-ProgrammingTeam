# Another Candies
# https://open.kattis.com/contests/jesw36/problems/anothercandies

for _ in range(int(input())):
    input()
    candies = [int(input())for _ in range(int(input()))]
    print(['YES','NO'][sum(candies)%len(candies)!=0])