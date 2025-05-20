# The CCSC
# python The_CCSC.py < CCSCin.txt > ccscout_test.txt && fc ccscout.txt ccscout_test.txt

class Node:
    def __init__(self):
        self.representative = None


class Union_Find:
    def __init__(self,num_child):
        self.representative = [i for i in range(num_child)]
        self.rank = [0 for _ in range(num_child)]
        self.jar = [0 for _ in range(num_child)]
        self.glass = [0 for _ in range(num_child)]
        self.num_mem = [1 for _ in range(num_child)]
    def debug(self):
        print('REP:',self.representative)
        print('RANK',self.rank)
        print('JAR',self.jar)
        print('GLASS',self.glass)
        print('NUM_MEM',self.num_mem)
    def find(self, value):
        if value != self.representative[value]:
            self.representative[value] = self.find(self.representative[value])
        return self.representative[value]
    def union(self,p1,p2):
        rep1 = self.find(p1)
        rep2 = self.find(p2)
        if rep1==rep2:
            return
        if self.rank[rep1]<self.rank[rep2]:
            self.representative[rep1] = rep2
            if self.rank[rep1] == self.rank[rep2]:
                self.rank[rep1] += 1
            self.bring(rep2,self.jar[rep1],self.glass[rep1])
            self.num_mem[rep2] += self.num_mem[rep1]
        else:
            self.representative[rep2] = rep1
            if self.rank[rep1] == self.rank[rep2]:
                self.rank[rep1] += 1
            self.bring(rep1,self.jar[rep2],self.glass[rep2])
            self.num_mem[rep1] +=self.num_mem[rep2]
    def bring(self,child,njar,nglass):
        self.glass[child] += nglass
        self.jar[child] += njar

def run():
    num_child = int(input())
    # global Children
    sum_jar = 0
    sum_glass = 0
    Children = Union_Find(num_child)
    for c in range(num_child):
        Children.bring(c,*map(int,input().split()))
    num_pair = int(input())
    for __ in range(num_pair):
        Children.union(*map(int,input().split()))
    for i in range(num_child):
        if i==Children.find(i):
            sum_jar+=Children.jar[i]
            sum_glass+=Children.glass[i]
            if Children.jar[i]%Children.num_mem[i]!=0 or Children.glass[i]%Children.num_mem[i]!=0 or Children.jar[i]<Children.num_mem[i] or Children.glass[i]<Children.num_mem[i]:
                return 'no'
    if sum_jar==num_child and sum_glass==num_child*5:
        return 'yes'
    else:
        return 'no'

# sample_out = open('ccscout.txt').read().splitlines()
# for i in range(1,int(input())+1):
#     answer = f"Case #{i}: {run()}"
#     # print(f"Case #{i}: {run()}")
#     if answer!= sample_out[i-1]:
#         print(f"Case #{i}: BAD")
#         Children.debug()
#         print(f'Should be: {sample_out[i-1]}, not {answer}')

for i in range(1,int(input())+1):
    print(f"Case #{i}: {run()}")


