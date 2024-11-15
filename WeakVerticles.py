#input()
final = []
i = int(input())
while i != -1:

    answer = []

    for j in range(0,i):

        tmaj = list(map(int ,input().split(" ")))
        count = 0

        for k in range(0,i):
            if tmaj[k] == int(1):
                count+=1

        if count < 2:
            answer.append(j)

    final.append(answer)

    i = int(input())
    
print(final)