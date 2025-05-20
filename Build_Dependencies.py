# Build Dependencies

class Node:
    def __init__(self,name):
        self.name = name
        self.parent = set()
        self.child = set()
class TopologicalSorting:
    def __init__(self,num):
        self.all = [-1 for _ in range(num)]
        self.mapping = dict()
        self.current_map = 0
    def add(self,slave,**masters):
        if slave not in self.mapping:
            self.mapping[slave] = self.current_map
            self.current_map += 1
            node_slave = Node(slave)
        else:
            node_slave = self.all[self.mapping[slave]]
        for master in masters:
            if master not in self.mapping:
                self.mapping[master] = self.current_map
                self.current_map += 1
                node_master = Node(master)
            else:
                node_master = self.all[self.mapping[master]]
            node_master.child


# Memory Limit Exceeded Solution
# from collections import defaultdict
# from collections import deque

# all = defaultdict()
# for _ in range(int(input())):
#         line = input().split()
#         slave = line.pop(0)[:-1]
#         for master in line:
#             if master not in all:
#                 all[master]={slave}
#             else:
#                 all[master].add(slave)
# printed = set()
# myQ = deque()
# change = input()
# myQ.append(change)
# while myQ:
#     new = myQ.popleft()
#     if new not in printed:
#         print(new)
#         printed.add(new)
#     if new in all:
#         for master in all[new]:
#             myQ.append(master)