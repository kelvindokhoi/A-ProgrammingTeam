# Akcija
# https://open.kattis.com/contests/jesw36/problems/akcija

books = sorted(-int(input()) for _ in range(int(input())))
numgr = len(books)//3
price = 0
for i in range(numgr):
    price += books[i*3]+books[i*3+1]
price += sum(books[(numgr)*3:])
print(-price)
# print(books)
