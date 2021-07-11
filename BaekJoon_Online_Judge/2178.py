import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [[0 for _ in range(M+2)] for _ in range(N+2)]
for i in range(1, N+1):
    line = input()
    for j in range(1, M+1):
        grid[i][j] = line[j-1]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
q = deque()
q.append((1, 1))
grid[1][1] = 1
while q:
    x, y = q.popleft()
    for i in range(4):
        new_x, new_y = x + dx[i], y + dy[i]
        if 1<=new_x<=N and 1<=new_y<=M and grid[new_x][new_y] == '1':
            grid[new_x][new_y] = int(grid[x][y]) + 1
            q.append((new_x, new_y))

print(grid[N][M])