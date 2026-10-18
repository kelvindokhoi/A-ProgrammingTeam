
# exceedinglimits.py
# Exceeding Limits
# https://open.kattis.com/problems/exceedinglimits

import sys
import heapq

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

num_intersections, num_roads, time_within = map(int,input().split())
road_map = []
for _ in range(num_roads):
    inter_a, inter_b, length, speed_limit = map(int, input().split())
    road_map.append((inter_a-1, inter_b-1, length, speed_limit))

def speedlimit_to_adj(road_map, num_intersections, over_speed):
    adj = [[] for _ in range(num_intersections)]
    for inter_a, inter_b, length, speed_limit in road_map:
        cost = length / (speed_limit + over_speed)
        adj[inter_a].append((inter_b, cost))
        adj[inter_b].append((inter_a, cost))
    return adj

def binary_search_over_speed(road_map, num_intersections, target_time):
    low = 0.0
    high = 2**63-1  # Upper bound for over_speed
    precision = 1e-6

    while high - low > precision:
        mid = (low + high) / 2
        adj = speedlimit_to_adj(road_map, num_intersections, mid)
        dists = dijkstra(adj, 0)  # Assuming source is intersection 0
        if dists[num_intersections - 1] <= target_time:
            high = mid
        else:
            low = mid
    return high

print(binary_search_over_speed(road_map, num_intersections, time_within))