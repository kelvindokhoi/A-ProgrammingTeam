# vote
# Popular Vote
def test():
    n=int(input()) #number of candidates
    box=[int(input())for _ in" "*n]
    sumVote=sum(box)
    maxVote=max(box)
    w=[i for i in range(n) if box[i]==maxVote]
    if len(w)>1:
        print("no winner")
    else:print(f"majority winner {w[0]+1}"if box[w[0]]*2>sumVote else f"minority winner {w[0]+1}")

T=int(input()) #test cases
for i in" "*T:
    test()
