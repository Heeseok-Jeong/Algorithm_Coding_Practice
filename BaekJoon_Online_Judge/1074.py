from math import log2

N, r, c = map(int, input().split())

grid = [[0 for _ in range(2**N)] for _ in range(2**N)]

def make_z_grid(n, x, y):
    if n == 1:
        base = 0
        if not (x == 0 and y == 0):
            if x == 0:
                log_y = log2(y)
                if log_y == int(log_y):
                    base = 2**y
            elif y == 0:
                log_x = log2(x)
                if log_x == int(log_x):
                    base = 2**(x+1)
            else:
                log_x = log2(x)
                log_y = log2(y)
                base = 
        grid[x][y] = base
        grid[x][y+1] = base + 1
        grid[x+1][y] = base + 2
        grid[x+1][y+1] = base + 3


    else:
        make_z_grid(n-1, x, y)
        make_z_grid(n-1, x, y+2**(n-1))
        make_z_grid(n-1, x+2**(n-1), y)
        make_z_grid(n-1, x+2**(n-1), y+2**(n-1))

make_z_grid(N, 0, 0)

for line in grid:
    print(line)

print(grid[r][c])

