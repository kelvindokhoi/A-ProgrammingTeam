# Shuffling Along
# shuffling

def checkdeck(deck,len_d):
    old=deck[0]
    for i in range(1,len_d):
        if deck[i]<old:
            return False
        old=deck[i]
    return True

def shuffle(max,mode='in'):
    if max==0 or max==1:
        return 1
    totalshuffle = 1
    if max&1:
        mid=max//2+1
    else:mid=max//2
    deck=[*range(max)]
    if mode=='out':
        if max&1:
            new=[0]*max
            for i in range(mid-1):
                new[i*2]=deck[i]
                new[i*2+1]=deck[i+mid]
            new[max-1]=deck[mid-1]
            deck=new
            while not checkdeck(deck,max):
                totalshuffle+=1
                new=[0]*max
                for i in range(mid-1):
                    new[i*2]=deck[i]
                    new[i*2+1]=deck[i+mid]
                new[max-1]=deck[mid-1]
                deck=new
        else:
            new=[0]*max
            for i in range(mid):
                new[i*2]=deck[i]
                new[i*2+1]=deck[i+mid]
            deck=new
            while not checkdeck(deck,max):
                totalshuffle+=1
                new=[0]*max
                for i in range(mid):
                    new[i*2]=deck[i]
                    new[i*2+1]=deck[i+mid]
                deck=new
    else:
        # mode = in
        if max&1:
            new=[0]*max
            for i in range(mid-1):
                new[i*2+1]=deck[i]
                new[i*2]=deck[i+mid-1]
            new[max-1]=deck[max-1]
            deck=new
            while not checkdeck(deck,max):
                totalshuffle+=1
                new=[0]*max
                for i in range(mid-1):
                    new[i*2+1]=deck[i]
                    new[i*2]=deck[i+mid-1]
                new[max-1]=deck[max-1]
                deck=new
        else:
            new=[0]*max
            for i in range(mid):
                new[i*2+1]=deck[i]
                new[i*2]=deck[i+mid]
            deck=new
            while not checkdeck(deck,max):
                totalshuffle+=1
                new=[0]*max
                for i in range(mid):
                    new[i*2+1]=deck[i]
                    new[i*2]=deck[i+mid]
                deck=new
    return totalshuffle
a,b=input().split()
print(shuffle(int(a),b))