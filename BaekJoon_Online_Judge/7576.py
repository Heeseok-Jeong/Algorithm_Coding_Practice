import sys
from copy import deepcopy

input = sys.stdin.readline

M, N = map(int, input().split())
grid = [[-1 for _ in range(M+2)]]

for _ in range(N):
    line = [-1] + list(map(int, input().split())) + [-1]
    grid.append(line)
grid.append([-1 for _ in range(M+2)])

locs = []
for i in range(N+2):
    for j in range(M+2):
        if grid[i][j] == 1:
            locs.append((i, j))

result = -1
temp = []
d_x = [-1, 0, 1, 0]
d_y = [0, 1, 0, -1]
while True:
    result += 1
    for x, y in locs:
        for i in range(4):
            if grid[x + d_x[i]][y + d_y[i]] == 0:
                grid[x + d_x[i]][y + d_y[i]] = 1
                temp.append((x + d_x[i], y + d_y[i]))
    if temp:
        locs = deepcopy(temp)
        temp.clear()
    else:
        break

for line in grid:
    if 0 in line:
        result = -1

print(result)
