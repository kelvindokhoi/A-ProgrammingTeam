# Karte
# karte
allcards = {i:set() for i in 'PKHT'}
robot_in = input()
for i in range(0,len(robot_in),3):
    suit,number = robot_in[i],robot_in[i+1:i+3]
    # print(suit,number)
    if number in allcards[suit]:
        print('GRESKA')
        exit()
    else:
        allcards[suit].add(number)
print(*[13-len(allcards[p]) for p in 'PKHT'])