import math

N, r, c = map(int, input().split())

grid = [[0 for _ in range(2**N)] for _ in range(2**N)]

def make_z_grid(n, x, y):
    if n == 1:
        x_value, y_value = 0, 0
        if x != 0:
            e_x = int(math.log(x, 2))
            x_value = 2**(2*e_x + 1) if 2**e_x == x else grid[e_x][y] + grid[x-e_x][y]
            
        if y != 0:
            e_y = int(math.log(y, 2))
            y_value = 2**(2*e_y) if 2**e_y == y else grid[x][e_y] + grid[x][y-e_y]

        base = 0
        if not (x == 0 and y == 0):
            e_x, e_y = 0, 0
            if x != 0:
                e_x = int(math.log(x, 2))
            if y != 0:
                e_y = int(math.log(y, 2))
            base = grid[x-e_x][y-e_y] + grid[e_x][e_y]

        grid[x][y] = base
        grid[x][y+1] = base+1
        grid[x+1][y] = base+2
        grid[x+1][y+1] = base+3

    # if n == 0:
        # if x != 0:
        #     e_x = int(math.log(x, 2))
        # if y != 0:
        #     e_y = int(math.log(y, 2))

    #     if x == 0 and y == 0:

    #     grid[x][y] = 
    else:
        make_z_grid(n-1, x, y)
        make_z_grid(n-1, x, y+2**(n-1))
        make_z_grid(n-1, x+2**(n-1), y)
        make_z_grid(n-1, x+2**(n-1), y+2**(n-1))

make_z_grid(N, 0, 0)

for line in grid:
    print(line)

print(grid[r][c])
