# Zipf's Law

import re

def calc_occr(listofall,num):
    myans=dict()
    outp=[]
    for case in listofall:
        if case in myans:
            myans[case]+=1
        else:
            myans[case]=1
    for i in myans.keys():
        if myans[i]==num:
            outp.append(i)
    return outp



while True:
    try:
        min_occr = int(input())
        listofall=[]
        while True:
            n=input()
            if n=="EndOfText":
                break
            k=re.sub(r'[^a-zA-Z]',' ',n.lower()).split()
            if k:
                listofall+=k
        final = sorted(calc_occr(listofall,min_occr))
        if final:
            for w in final:
                print(w)
        else:
            print("There is no such word.")
    except:
        break