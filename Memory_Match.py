# Memory Match
# memorymatch

N = int(input())
K = int(input())
cards = dict()
non_score = set()
# set the cards
score=0
for _ in ' '*K:
    pos1,pos2,val1,val2=input().split()
    pos1=int(pos1)
    pos2=int(pos2)
    if val1==val2:
        non_score.add(val1)
        cards[val1]={pos1,pos2}
    if val1 in cards:
        if not isinstance(cards[val1],set):
            if pos1!=cards[val1]:
                cards[val1]={cards[val1],pos1}
    else:
        cards[val1]=pos1
    if val2 in cards:
        if not isinstance(cards[val2],set):
            if pos2!=cards[val2]:
                cards[val2]={cards[val2],pos2}
    else:
        cards[val2]=pos2
no_couple = 0
for key in cards.keys():
    if isinstance(cards[key],set) and key not in non_score:
        score+=1
        # print(key)
    if isinstance(cards[key],int):
        no_couple+=1
if no_couple==0 and N-len(cards)*2==2:
    score+=1
if N-len(cards)*2==0:
    score+=no_couple

print(score)
# print(cards)
# print(non_score)

# earth mars sun 4 moon sun earth 8