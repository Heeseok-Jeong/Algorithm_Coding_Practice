from copy import deepcopy
from itertools import combinations
from collections import deque

d_x = [-1, 0, 1, 0]
d_y = [0, 1, 0, -1]

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def spread_virus(temp_grid, virus_loc):
    while virus_loc:
        row, col = virus_loc.popleft()
        temp_grid[row][col] = 2

        for i in range(4):
            new_row = row+d_x[i]
            new_col = col+d_y[i]
            if 0 <= new_row < N and 0 <= new_col < M:
                if temp_grid[new_row][new_col] == 0:
                    virus_loc.append((new_row, new_col))            

def count_empty_rooms(temp_grid):
    count = 0
    for i in range(N):
        for j in range(M):
            if temp_grid[i][j] == 0:
                count += 1
    return count

empty_list = []
initial_virus_loc = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            empty_list.append((i, j))
        elif grid[i][j] == 2:
            initial_virus_loc.append((i, j))
combis = list(combinations(empty_list, 3))

result = 0
for a, b, c in combis:
    temp_grid = deepcopy(grid)
    temp_grid[a[0]][a[1]] = 1
    temp_grid[b[0]][b[1]] = 1
    temp_grid[c[0]][c[1]] = 1

    spread_virus(temp_grid, deque(initial_virus_loc))
    result =  max(result, count_empty_rooms(temp_grid))

print(result)
