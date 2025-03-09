# A Classy Problem

import heapq

class Person():
    def __init__(self,name,classtring):
        self.name = name
        self.myclass = classtring.split('-')
        self.mylen = len(self.myclass)
    def __str__(self):return self.name
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
        bigger,smaller=0,0
        for i in range(len(n1)-1,-1,-1):
            if n1[i]>n2[i]:bigger=1;break
            if n1[i]<n2[i]:smaller=1;break
        if bigger:return True
        if smaller:return False
        return self.name<other.name

for _ in' '*int(input()):
    myheap = []
    people = int(input())
    allmember = []
    for i in' '*people:
        name,cls,_ = input().split()
        newPerson = Person(name[:-1],cls)
        heapq.heappush(myheap,newPerson)
    for i in' '*people:print(heapq.heappop(myheap))
    print('==============================')