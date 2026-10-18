# to run:
#  python Soviet_Union_Find.py < Soviet_Union_Find_in.txt
class DisjointUnionSets:
    def __init__(self, n):
        self.parent = list(range(n))
        self.n = n

    def find(self, i):
        if self.parent[i]==i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unionSets(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)

        if xRoot == yRoot:
            return

        self.parent[yRoot] = xRoot
    
    def SovietBreakdown(self,x):
        xRoot = self.find(x)
        for i in range(self.n):
            if self.find(i) == xRoot:
                self.parent[i] = i

n_region, q_queries = map(int,input().split())
ourU = DisjointUnionSets(n_region)
for _ in range(q_queries):
    inp = input()
    if inp[0]=="a":
        _,a,b = inp.split()
        a,b = int(a)-1,int(b)-1
        ourU.unionSets(a,b)
        # print(ourU.parent)
    elif inp[0]=="b":
        _,a = inp.split()
        a = int(a)-1
        ourU.SovietBreakdown(a)
        # print(ourU.parent)
    else:
        _,a = inp.split()
        a = int(a)-1
        print(ourU.find(a)+1)
        # print(f"parent of {a} is {ourU.find(a)}, {ourU.parent}")