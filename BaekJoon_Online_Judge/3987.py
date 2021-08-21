import copy

OUT = "O"
BLACKHOLE = "C"
PLANET1 = "\\"
PLANET2 = "/"

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
direction = ["U", "R", "D", "L"]

N, M = map(int, input().split())

grid_init = [[OUT] * (M+2)]
for _ in range(N):
    line = [OUT]
    for x in input():
        line.append(x)
    line += [OUT]
    grid_init.append(line)
grid_init.append([OUT] * (M+2))

start = tuple(map(int, input().split()))
results = []

for d in range(4):
    time = 0
    x, y = start
    grid = copy.deepcopy(grid_init)

    while True:
        time += 1

        if time > 2*N*M:
            time = "Voyager"
            break

        x += dx[d]
        y += dy[d]

        if grid[x][y] in [BLACKHOLE, OUT]:
            break
        elif grid[x][y] == PLANET1:
            if d == 0:
                d = 3
            elif d == 3:
                d = 0

            if d == 1:
                d = 2
            elif d == 2:
                d = 1
        elif grid[x][y] == PLANET2:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0

            if d == 2:
                d = 3
            elif d == 3:
                d = 2
    
    results.append(time)

result_direction = direction[0]
result_time = 0

for i in range(4):
    if "Voyager" == results[i]:
        result_direction = direction[i]
        result_time = results[i]
        break
    
    if result_time < results[i]:
        result_direction = direction[i]
        result_time = results[i]

print(result_direction)
print(result_time)
