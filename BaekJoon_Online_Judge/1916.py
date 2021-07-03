import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    f, t, c = map(int, input().split())
    graph[f].append((t, c))

FROM, TO = map(int, input().split())
table = [INF] * (N+1)
table[FROM] = 0

q = []
heapq.heappush(q, (0, FROM))

while q:
    dist, now = heapq.heappop(q)
    if dist > table[now]:
        continue
    
    for to, cost in graph[now]:
        if table[to] > dist + cost:
            table[to] = dist + cost
            heapq.heappush(q, (table[to], to))

print(table[TO])