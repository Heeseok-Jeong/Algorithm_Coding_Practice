from collections import deque
import sys

INF = 100001

input = lambda : sys.stdin.readline().rstrip()

n, k = map(int, input().split())
map = [[INF, 0] for _ in range(INF)]
dq = deque([n])
map[n] = [0, 1]

while dq:
    x = dq.popleft()
    for nx in [x-1, x+1, x*2]:
        if 0 <= nx < INF:
            if map[nx][0] == INF:
                map[nx][0] = map[x][0] + 1
                map[nx][1] = map[x][1]
                dq.append(nx)
            elif map[nx][0] == map[x][0] + 1:
                map[nx][1] += map[x][1]

print(map[k][0])
print(map[k][1])
