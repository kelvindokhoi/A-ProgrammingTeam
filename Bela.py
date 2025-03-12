# Bela
# bela

dominant = {a:b for a,b in zip([*'AKQJT987'],[11,4,3,20,10,14,0,0])}
nondominant = {a:b for a,b in zip([*'AKQJT987'],[11,4,3,2,10,0,0,0])}

hands,suit=input().split()
score=0
for i in range(int(hands)):
    for _ in range(4):
        a,b=input()
        if b==suit:
            score+=dominant[a]
        else:
            score+=nondominant[a]
print(score)