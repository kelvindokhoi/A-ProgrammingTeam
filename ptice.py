# ptice

a,b=int(input()),input()
p=[sum(b[i]==x[i%len(x)]for i in range(a))for x in["ABC","BABC","CCAABB"]]
print(max(p),*[n for n,s in zip(["Adrian","Bruno","Goran"],p)if s==max(p)],sep='\n')



"""a=int(input());b=input()
A,B,G="ABC","BABC","CCAABB"
p=[sum(b[i]==x[i%len(x)]for i in range(a))for x in[A,B,G]]
m=max(p);print(m)
print(*[n for i,n in enumerate(["Adrian","Bruno","Goran"])if p[i]==m],sep="\n")"""

"""a=int(input());b=input()
A="ABC";B="BABC";G="CCAABB"
p=[sum(b[i]==x[i%len(x)]for i in range(a))for x in[A,B,G]]
m=max(p);print(m)
for i in range(3):
 if p[i]==m:print(["Adrian","Bruno","Goran"][i])"""

"""a=int(input());b=input()
A="ABC";B="BABC";G="CCAABB"
p=[sum(b[i]==x[i%len(x)]for i in range(a))for x in[A,B,G]]
m=max(p);print(m)
for i in range(3):
 if p[i]==m:print(["Adrian","Bruno","Goran"][i])"""



"""a=int(input());b=[*input()]
pA=pB=pG=0
A=["A","B","C"]
B=['B','A','B','C']
G=['C','C','A','A','B','B']
iA=iter(A);iB=iter(B);iG=iter(G)
for i in range(a):
    try:
        if b[i]==next(iA):pA+=1
    except:
        iA=iter(A)
        if b[i]==next(iA):pA+=1
    try:
        if b[i]==next(iB):pB+=1
    except:
        iB=iter(B)
        if b[i]==next(iB):pB+=1
    try:
        if b[i]==next(iG):pG+=1
    except:
        iG=iter(G)
        if b[i]==next(iG):pG+=1
m=max(pA,pB,pG)
print(m)
if pA==m:print("Adrian")
if pB==m:print("Bruno")
if pG==m:print("Goran")"""