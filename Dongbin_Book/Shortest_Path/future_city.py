INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

answer = 0

for layover in range(1, n+1):
    for departure in range(1, n+1):
        for to in range(1, n+1):
            graph[departure][to] = min(graph[departure][to], graph[departure][layover] + graph[layover][to])

answer = graph[1][k] + graph[k][x]
if answer >= INF:
    print(-1)
else:
    print(answer)
