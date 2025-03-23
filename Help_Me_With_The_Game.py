# Help Me With The Game

white = []
black = []
order = 'KQRBNP'
def getchar(string):
    color = 'w'if string[1].isupper() else 'b'
    return (string[1].upper(),color) if string[1].isalpha() else False
def buildstring(lst):
    newlst = []
    for i in lst:
        if i[0]!='P':
            newlst.append(i)
        else:
            newlst.append(i[1:])
    return newlst

for _ in range(8):
    input()
    n = input().split(sep='|')
    for i in range(8):
        nchar = n[i+1]
        converted = getchar(nchar)
        if isinstance(converted,tuple):
            if converted[1]=='w':
                white.append(converted[0]+chr(i+ord('a'))+str(8-_))
            else:
                black.append(converted[0]+chr(i+ord('a'))+str(8-_))
input()
white.sort(key= lambda x: (order.index(x[0]),x[2],x[1]))
print('White:',','.join(buildstring(white)))
black.sort(key= lambda x: (order.index(x[0]),-ord(x[2]),ord(x[1])))
print('Black:',','.join(buildstring(black)))