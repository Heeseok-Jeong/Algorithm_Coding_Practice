import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    departure, to, cost = map(int, input().rstrip().split())
    graph[departure].append((to, cost))

distance = [INF for _ in range(n+1)]

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for other in graph[now]:
            # print(other)
            cost = dist + other[1]
            if distance[other[0]] > cost:
                distance[other[0]] = cost
                heapq.heappush(q, (cost, other[0]))

dijkstra(c)
received_num = 0
max_num = 0
for i in range(1, n+1):
    if distance[i] < INF and i is not c:
        received_num += 1
        max_num = max(max_num, distance[i])

print(received_num, max_num)

