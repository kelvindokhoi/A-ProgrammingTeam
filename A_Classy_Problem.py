# A Classy Problem


import heapq

def score(cls):
    pclass=0
    for i in cls:
            curr = 1 if i=='upper' else 0.5 if i=='middle' else 0
            pclass = (pclass + curr)/2
    # pclass = sum(1 if i=='upper' else 0 if i=='middle' else -1 for i in cls)/len(cls)
    return pclass

class Person():
    def __init__(self,name,classtring):
        self.name = name
        self.myclass = classtring.split('-')
        self.mylen = len(self.myclass)
        
    def __str__(self):
        return self.name
    def __lt__(self,other):
        if self.mylen>other.mylen:
            n1=self.myclass
            n2=['middle']*(self.mylen-other.mylen)+other.myclass
        elif other.mylen>self.mylen:
            n2=other.myclass
            n1=['middle']*(other.mylen-self.mylen)+self.myclass
        else:
            n2=other.myclass
            n1=self.myclass
        bigger=False
        smaller=False
        for i in range(len(n1)-1,-1,-1):
            if n1[i]>n2[i]:
                bigger=True
                break
            if n1[i]<n2[i]:
                smaller=True
                break
        if bigger:
            return True
        if smaller:
            return False
        s1=score(n1)
        s2=score(n2)
        if s1>s2:
            return True
        if s2>s1:
            return False
        return self.name<other.name
        

cases=int(input())
for case in range(cases):
    myheap = []
    heapq.heapify(myheap)
    people = int(input())
    allmember = []
    for i in range(people):
        fullstr=input()
        name,clss,_ = fullstr.split()
        name = name[:-1]
        newPerson = Person(name,clss)
        heapq.heappush(myheap,newPerson)
    for i in range(people):
        print(heapq.heappop(myheap))
    print('==============================')
