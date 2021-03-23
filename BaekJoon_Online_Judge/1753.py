import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

distance = [INF for _ in range(V+1)]

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for other_v, other_dist in graph[now]:
        cost = distance[now] + other_dist
        if distance[other_v] > cost:
            distance[other_v] = cost
            heapq.heappush(q, (distance[other_v], other_v))

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
