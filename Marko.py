# Marko
# https://open.kattis.com/contests/kfmmw4/problems/marko

count = int(input())
letters = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
dictionary = dict()
for i in range(2,10):
    for c in iter(letters[i-2]):
        dictionary[c]=str(i)


abc = []
for _ in range(count):
    ppp= input()
    abc.append(''.join(dictionary[a]for a in iter(ppp)))
c = 0
k = input()
for x in abc:
    if x==k:
        c+=1
print(c)

# print(dictionary)