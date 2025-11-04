import sys
from collections import defaultdict, deque

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

n = int(input())
strings = [input().strip() for _ in ' '*n]

# Step 1: TRIE for FULL prefix check
root = TrieNode()
impossible = False
for s in strings:
    node = root
    for c in s:
        # Shorter earlier: OK
        if node.is_end:
            pass
        if c not in node.children:
            node.children[c] = TrieNode()
        node = node.children[c]
    # Longer earlier? IMPOSSIBLE!
    if node.children:
        impossible = True
        break
    node.is_end = True

if impossible:
    print('impossible')
else:
    # Step 2: Build graph from CONSECUTIVE pairs ONLY
    graph = defaultdict(list)
    indeg = {chr(ord('a') + i): 0 for i in range(26)}
    for i in range(n - 1):
        s1, s2 = strings[i], strings[i + 1]
        minl = min(len(s1), len(s2))
        found_diff = False
        for j in range(minl):
            if s1[j] != s2[j]:
                u, v = s1[j], s2[j]
                if v not in graph[u]:
                    graph[u].append(v)
                    indeg[v] += 1
                found_diff = True
                break
        if not found_diff:
            # Prefix case (redundant, trie caught)
            if len(s1) > len(s2):
                impossible = True
                break

    if impossible:
        print('impossible')
    else:
        # Step 3: Kahn's Topo Sort
        q = deque(c for c in indeg if indeg[c] == 0)
        order = []
        while q:
            u = q.popleft()
            order.append(u)
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        if len(order) == 26:
            print(''.join(order))
        else:
            print('impossible')