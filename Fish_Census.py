# Fish Census
import re

def kmp(t,p):
    n,m=len(t),len(p);l=[0]*m;j=0
    if m<1:return[0]*(n>-1)
    if n<1:return[]
    for i in range(1,m):
        while j and p[i]!=p[j]:j=l[j-1]
        j+=p[i]==p[j];l[i]=j
    i=j=0;r=[]
    while i<n:
        while i<n and j<m and t[i]==p[j]:i,j=i+1,j+1
        if j==m:r+=[i-j];j=l[j-1]
        elif j:j=l[j-1]
        else:i+=1
    return r

for _ in' '*int(input()):
    fish_tank = [re.sub(r'{+','{',re.sub(r'}+','}',re.sub(r'\(+','(',re.sub(r'\)+',')',input())))) for _ in' '*int(input().split()[0])]
    flounder = 0
    koi = 0
    trout = 0
    for line in fish_tank:
        flounder += (len(kmp(line,r'><(">'))+len(kmp(line,r'<")><'))+len(kmp(line,r'<"}><'))+len(kmp(line,r'><{">')))
        koi += (len(kmp(line,r'><(*>')) + len(kmp(line,r'<*)><')) + len(kmp(line,r'<*}><'))+ len(kmp(line,r'><{*>')))
        trout += (len(kmp(line,r"><{'>")) + len(kmp(line,r"<'}><")) + len(kmp(line,r"<')><")) + len(kmp(line,r"><('>")))
    print(flounder,koi,trout)