n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, list(input()))))


def browse(i, j):
    if i < 0 or i >=n or j < 0 or j >= m or graph[i][j] == 1:
        return
    graph[i][j] = 1
    browse(i-1, j)
    browse(i+1, j)
    browse(i, j-1)
    browse(i, j+1)


answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            browse(i, j)
            answer += 1

print(answer)
