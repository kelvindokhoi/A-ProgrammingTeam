# Connect the Dots
# connectthedots
# python Connect_the_Dots.py < connectthedots_in.txt

def changing(array,start_x,start_y,end_x,end_y):
    # in the same row 
    if start_x==end_x:
        if start_y>end_y:
            start_y,end_y = end_y,start_y
        for i in range(start_y+1,end_y):
            if array[start_x][i]=='.':
                array[start_x][i] = '-'
            elif array[start_x][i]=='|':
                array[start_x][i] = '+'
            else:
                pass
    if start_y==end_y:
        if start_x>end_x:
            start_x,end_x = end_x,start_x
        for i in range(start_x+1,end_x):
            if array[i][start_y]=='.':
                array[i][start_y] = '|'
            elif array[i][start_y]=='-':
                array[i][start_y] = '+'
            else:
                pass

def find(array,element):
    i=len(array)
    j = len(array[0])
    for m in range(i):
        for n in range(j):
            if array[m][n]==element:
                return (m,n)

def mapmaking(array,maxx):
    if maxx=='.':return
    total = [*map(str,range(0,10)),*'abcdefghijklmnopqrstuvwxyz',*'abcdefghijklmnopqrstuvwxyz'.upper()]
    total = total[:total.index(maxx)+1]
    # print(total)
    for i in range(len(total)-1):
        changing(array,*find(array,total[i]),*find(array,total[i+1]))
        # print(*[''.join(x) for x in array],sep= '\n',end = '\n')
    return

curr_max = '.'
array = []
allchars = ['.',*map(str,range(0,10)),*'abcdefghijklmnopqrstuvwxyz',*'abcdefghijklmnopqrstuvwxyz'.upper()]
while True:
    try:
        newline = input()
        if newline == '':
            mapmaking(array,curr_max)
            print(*[''.join(x) for x in array],sep= '\n',end = '\n')
            print()
            array = []
            curr_max = '.'
        else:
            curr_max = allchars[max(allchars.index(curr_max),allchars.index(max(newline,key = lambda x: allchars.index(x))))]
            array.append(list(newline))
    except EOFError:
        mapmaking(array,curr_max)
        print(*[''.join(x) for x in array],sep= '\n',end = '\n')
        break