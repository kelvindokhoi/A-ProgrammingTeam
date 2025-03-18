# Chess
# chess

translator = {i:j for i,j in zip('ABCDEFGH',[int(n)for n in '12345678'])}
revert = {i:j for i,j in zip([int(n)for n in '12345678'],'ABCDEFGH')}
def allpossible(move):
    moveset = set()
    temp = move
    while 'H'>=temp[0]>='A' and 8>=int(temp[1])>=1:
        moveset.add(temp)
        temp = chr(ord(temp[0])+1)+str(int(temp[1])+1)
    temp = move
    while 'H'>=temp[0]>='A' and 8>=int(temp[1])>=1:
        moveset.add(temp)
        temp = chr(ord(temp[0])-1)+str(int(temp[1])+1)
    temp = move
    while 'H'>=temp[0]>='A' and 8>=int(temp[1])>=1:
        moveset.add(temp)
        temp = chr(ord(temp[0])+1)+str(int(temp[1])-1)
    temp = move
    while 'H'>=temp[0]>='A' and 8>=int(temp[1])>=1:
        moveset.add(temp)
        temp = chr(ord(temp[0])-1)+str(int(temp[1])-1)
    return moveset
    
for i in' '*int(input()):
    c1,n1,c2,n2 = input().split()
    n1=int(n1)
    n2=int(n2)
    if c1==c2 and n1==n2:
        print(0,c1,n1)
    else:
        intersection = allpossible(c1+str(n1))&allpossible(c2+str(n2))
        # print(f'intersection: {intersection}')
        if abs(int(translator[c1])+int(n1))==abs(int(translator[c2])+int(n2)):
            print(1,c1,n1,c2,n2)
        elif len(intersection)==0:
            print('Impossible')
            # print(allpossible(c1+str(n1)))
            # print(allpossible(c2+str(n2)))
        else:
            a=intersection.pop()
            print(2,c1,n1,a[0],a[1],c2,n2)
