totalCase = int(input())
answer = []

def atime(v1,v2, d):
    return int(round(2*d/(v1+v2)*3600,0))

def ftime(time):
    if time-(time//60)*60 < 10:
        return str(time//60)+":"+"0"+str(time-(time//60)*60)
    else:
        return str(time//60)+":"+str(time-(time//60)*60)

for i in range(totalCase):
    v1, v2, d = map(float, input().split(" "))
    answer.append(ftime(atime(v1, v2, d)))


for i in range(totalCase):
    print(answer[i])