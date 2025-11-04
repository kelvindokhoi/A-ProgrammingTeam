# Hacky Ordering
# https://open.kattis.com/problems/hackyordering

from collections import defaultdict,deque

strings = [input().strip() for _ in ' '*int(input())]

class Trie_Node:
    def __init__(self):
        self.children = dict()
        self.end = False

def build_Trie(strings:list)->Trie_Node|None:
    root = Trie_Node()
    for string in strings:
        current_level = root
        for character in string:
            if character not in current_level.children:
                current_level.children[character] = Trie_Node()
            current_level = current_level.children[character]
        if current_level.children:
            return None
        current_level.end = True
    return root

def build_constraint_graph(strings):
    graph = defaultdict(list)
    indeg = {chr(ord('a')+i):0 for i in range(26)}
    for i in range(len(strings)-1):
        s1,s2 = strings[i],strings[i+1]
        minimum_length = min(len(s1),len(s2))
        diff = False
        for j in range(minimum_length):
            if s1[j]!=s2[j]:
                u,v = s1[j],s2[j]
                if v not in graph[u]:
                    graph[u].append(v)
                    indeg[v] += 1
                diff = True
                break
        if not diff:
            if len(s1) > len(s2):
                return None
    return indeg,graph

def kahn_top_sort(strings:list):
    root = build_Trie(strings)
    if root is None:
        return None
    build_constaint_ouput = build_constraint_graph(strings)
    if build_constaint_ouput is None:
        return None
    indeg,graph = build_constaint_ouput
    q = deque(c for c in indeg if indeg[c]==0)
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    if len(order)==26:
        return ''.join(order)
    else:
        return None

result = kahn_top_sort(strings)
print(result if result is not None else 'impossible')


