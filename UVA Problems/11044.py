# 11044 - Searching for Nessy
for _ in range(int(input())):
    def search(x,y):
        return (x//3)*(y//3) + (x%3!=0)*(y//3) + (y%3!=0)*(x//3) + (x%3!=0)*(y%3!=0)

    x, y = map(int,input().split())
    x-=2
    y-=2
    print(search(x,y))