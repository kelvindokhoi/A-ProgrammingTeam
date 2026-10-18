# dfaisempty
# Deterministic Finite Automata - Is the Empty Language?
# https://open.kattis.com/problems/dfaisempty
import heapq,sys
def dijkstra(adj, src):

    V = len(adj)

    # Min-heap (priority queue) storing pairs of (distance, node)
    pq = []

    dist = [sys.maxsize] * V

    # Distance from source to itself is 0
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    # Process the queue until all reachable vertices are finalized
    while pq:
        d, u = heapq.heappop(pq)

        # If this distance not the latest shortest one, skip it
        if d > dist[u]:
            continue

        # Explore all neighbors of the current vertex
        for v, w in adj[u]:

            # If we found a shorter path to v through u, update it
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    # Return the final shortest distances from the source
    return dist
n_numstates,c_alphasize,s_inistate,f_numfinalstates = map(int,input().split())
alphabet = input()
*final_states, = map(lambda x: int(x)-1,input().split())
transitions = [list(map(lambda x: (int(x)-1,1),input().split())) for i in range(n_numstates)]
dist = dijkstra(transitions,s_inistate-1)
if any(dist[i]!=sys.maxsize for i in final_states):
    print("non-empty")
else:
    print("empty")