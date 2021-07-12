import sys

input = sys.stdin.readline

rippen = []
M, N, H = map(int, input().split())
grid = [[[-1 for _ in range(M+2)] for _ in range(N+2)] for _ in range(H+2)]
for i in range(1, H+1):
    for j in range(1, N+1):
        line = list(map(int, input().split()))
        for k in range(1, M+1):
            grid[i][j][k] = line[k-1]
            if grid[i][j][k] == 1:
                rippen.append((i, j, k))

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
day = 0
while rippen:
    new_rippen = []
    for z, x, y in rippen:
        for i in range(6):
            new_z, new_x, new_y = z + dz[i], x + dx[i], y + dy[i]
            if 1<=new_z<=H and 1<=new_x<=N and 1<=new_y<=M and grid[new_z][new_x][new_y] == 0:
                grid[new_z][new_x][new_y] = 1
                new_rippen.append((new_z, new_x, new_y))
    rippen = new_rippen
    day += 1

day -= 1
answer = day
for i in range(1, H+1):
    if answer == -1:
        break
    for j in range(1, N+1):
        if answer == -1:
            break
        for k in range(1, M+1):
            if grid[i][j][k] == 0:
                answer = -1
                break
                
print(answer)
