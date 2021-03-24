import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    begin, to, cost = map(int, input().split())
    graph[begin][to] = min(graph[begin][to], cost)

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print()
