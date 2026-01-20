# 13274 - Christmas Tree
# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=878&page=show_problem&problem=5198

# python UVA_Problems\13274-Christmas_Tree.py < UVA_Problems\13274_in.txt


for caseNo in range(int(input().strip())):
    Nnodes, Kchild = map(int,input().strip().split())
    children_count = [0]*Nnodes
    adjacency_list = {x:set() for x in range(Nnodes)}
    weight = [1]*Nnodes

    
    print(f"Case {caseNo+1}: {weight[0]}")



#failed code due to undirected tree assumption
# from collections import deque

# class Node:
#     def __init__(self):
#         self.numchild = 0
#         self.children = set()
#         self.parent = -1
#         self.weight = 0
#     def __str__(self) -> str:
#         return f"Node([numchild={self.numchild}, children={self.children}, parent={self.parent}, weight={self.weight}])"

# T = int(input().strip())
# for caseNo in range(T):
#     Nnodes, Kchild = map(int,input().strip().split())
#     tree = [Node() for _ in range(Nnodes)]
#     for _ in range(Nnodes-1):
#         u,v = map(int,input().strip().split())
#         parent = tree[u-1]
#         child = tree[v-1]
#         parent.children.add(v-1)
#         parent.numchild += 1
#         child.parent = u-1
#         while u!=-1:
#             tree[u].weight += 1
#             u = tree[u].parent
#     checklist = deque([0])
#     while checklist:
#         target = checklist.popleft()
#         if tree[target].numchild == Kchild:
#             continue
#         if tree[target].numchild < Kchild:
#             minus = tree[target].weight
#             p = tree[target].parent
#             if p!=-1:
#                 checklist.append(p)
#             tree[p].children.discard(target)
#             tree[target].parent = -1
#             while p!=-1:
#                 tree[p].weight -= minus
#                 p = tree[p].parent
#         elif tree[target].numchild > Kchild:
#             listchild = sorted([(tree[child].weight,child) for child in tree[target].children])
#             sum_minus = 0
#             target_children = listchild[:Kchild-tree[target].numchild]
#             for w,target_child in target_children:
#                 sum_minus += w
#                 tree[target_child].parent = -1
#             tree[target].children -= set([x[1] for x in target_children])
#             p = target
#             while p!=-1:
#                 tree[p].weight -= sum_minus
#                 p = tree[p].parent
#     print(f"Case {caseNo+1}: {tree[0].weight}")
#     print([x.__str__() for x in tree])