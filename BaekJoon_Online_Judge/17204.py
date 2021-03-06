N, K = map(int, input().split())
graph = [[int(input()), False] for _ in range(N)]

result = -1
node = 0
graph[node][1] = True
i = 0
while True:
    i += 1
    node = graph[node][0]

    if graph[node][1]:
        break
    graph[node][1] = True

    if node == K:
        result = i
        break

print(result)
    