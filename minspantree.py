# minspantree.py
# Minimum Spanning Tree
# python minspantree.py < minspantree_in.txt > minspantree_out.txt && fc minspantree_out.txt minspantree_sp_out.txt
import heapq

# Returns total weight of the Minimum Spanning Tree
def spanningTree(V, adj):

    # Min-heap storing (weight, vertex)
    pq = []
    visited = [False] * V
    res = 0

    # Start from node 0
    heapq.heappush(pq, (0, 0,0))    
    recorded_edge = []
    while pq:

        wt, u,v = heapq.heappop(pq)

        if visited[u]:
            continue

        res += wt
        if u!=v:
            recorded_edge.append([u,v]if u<v else [v,u])
        visited[u] = True

        # Push adjacent edges
        for v in adj[u]:
            if not visited[v[0]]:
                heapq.heappush(pq, (v[1], v[0],u))

    return res,recorded_edge


n_node,m_edges = map(int,input().split())
while not(n_node==m_edges==0):
    graph = [[] for _ in range(n_node)]
    for _ in ' '*m_edges:
        u,v,w = map(int,input().split())
        graph[u].append([v,w])
        graph[v].append([u,w])
    mst,rc_edge = spanningTree(n_node,graph)
    count = 0
    rc_edge = sorted(rc_edge)
    real_edges = [(u, v) for u, v in rc_edge if u != v]
    if len(real_edges) == n_node - 1:
        print(mst)
        for u, v in real_edges:
            print(u, v)
    else:
        print("Impossible")
    n_node,m_edges = map(int,input().split())
