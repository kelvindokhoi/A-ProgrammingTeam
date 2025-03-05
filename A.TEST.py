import math
from collections import deque

# Union-Find data structure for Kruskal's algorithm
class UnionFind:
    def __init__(self, n):
        # Initialize each node as its own parent
        self.parent = list(range(n))
        # Initialize rank for union by rank
        self.rank = [0] * n
    
    def find(self, x):
        # Find the root with path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Unite two sets by rank
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already in the same set
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[px] < self.rank[py]:
            self.parent[px] = py
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True  # Union successful

# Function to compute Euclidean distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Main program
scenario = 1
while True:
    # Read number of stones
    n = int(input())
    if n == 0:
        break  # Terminate on n = 0
    
    # Read coordinates of stones
    stones = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Step 1: Generate all possible edges
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(stones[i], stones[j])
            edges.append((d, i, j))
    
    # Step 2: Sort edges by distance
    edges.sort()
    
    # Step 3: Build MST using Kruskal's algorithm
    uf = UnionFind(n)
    mst_edges = []
    for edge in edges:
        d, u, v = edge
        if uf.union(u, v):
            mst_edges.append(edge)
            if len(mst_edges) == n - 1:
                break  # MST complete with n-1 edges
    
    # Step 4: Build adjacency list representation of MST
    mst_adj = [[] for _ in range(n)]
    for d, u, v in mst_edges:
        mst_adj[u].append((v, d))  # Add edge u -> v
        mst_adj[v].append((u, d))  # Add edge v -> u (undirected)
    
    # Step 5: BFS to find frog distance
    max_jump = [-1] * n  # Maximum jump needed to reach each node
    max_jump[0] = 0      # Start at Freddy's stone (index 0)
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v, w in mst_adj[u]:
            if max_jump[v] == -1:  # If unvisited
                max_jump[v] = max(max_jump[u], w)
                queue.append(v)
    
    frog_distance = max_jump[1]  # Max jump to Fiona's stone (index 1)
    
    # Step 6: Output result
    print(f"Scenario #{scenario}")
    print(f"Frog Distance = {frog_distance:.3f}")
    print()  # Blank line after each test case
    
    scenario += 1
    input()  # Read the blank line after each test case