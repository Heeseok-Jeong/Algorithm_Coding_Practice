n, m = map(int, input().split())
maze = [[0 for _ in range(m+1)]]
for _ in range(n):
    line = [0]
    line += list(map(int, input()))
    maze.append(line)

min_count = n*m

def browse(i, j, count):
    global min_count
    count += 1
    if i < 1 or i > n or j < 1 or j > m or maze[i][j] == 0:
        return

    if i == n and j == m:
        if min_count > count:
            min_count = count
            return

    maze[i][j] = 0
    browse(i-1, j, count)
    browse(i+1, j, count)
    browse(i, j-1, count)
    browse(i, j+1, count)


browse(1, 1, 0)
print(min_count)
