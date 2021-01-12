dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ways = ["U", "D", "L", "R"]
x, y = 1, 1

n = int(input())
commands = list(input().split())
for command in commands:
    for i in range(4):
        if ways[i] == command:
            nx = x + dx[i]
            ny = y + dy[i]
    if not (nx < 1 or nx > n or ny < 1 or ny > n):
        x = nx
        y = ny

print(x, y)
