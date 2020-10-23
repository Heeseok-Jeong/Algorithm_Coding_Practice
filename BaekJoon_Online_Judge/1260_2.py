from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
route = {}

# for _ in range(m):
#     start, to = map(int, input().split())
#     route[start] = route.get(start, []) + [to]
#     route[to] = route.get(to, []) + [start]
#
# for key in route.keys():
#     route[key].sort()
# print("route :", route)

info = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    start, to = map(int, input().split())
    info[start][to] = 1
    info[to][start] = 1
# print("info :", info)

#DFS
stack = [v]
visited = [False] * (n+1)
result = []
while stack:
    x = stack.pop()
    if not visited[x]:
        result.append(x)

        for i in range(n, 0, -1):
            if info[x][i] == 1 and not visited[i]:
                stack.append(i)
        # for to in route[x][::-1]:
        #     if not visited[to]:
        #         stack.append(to)
        visited[x] = True

print(' '.join(map(str, result)))

#BFS
dq = deque([v])
visited = [False] * (n+1)
result = []

while dq:
    x = dq.popleft()
    if not visited[x]:
        result.append(x)

        for i in range(1, n+1):
            if info[x][i] == 1 and not visited[i]:
                dq.append(i)
        # for to in route[x]:
        #     if not visited[to]:
        #         dq.append(to)
        visited[x] = True


print(' '.join(map(str, result)))
