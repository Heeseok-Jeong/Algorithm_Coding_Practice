n, m = map(int, input().split())
x, y, d = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
world[x][y] = 2
answer = 1

def turn_left():
    global d
    d -= 1
    if d < 0:
        d = 3

count = 1
while True:
    turn_left()
    # print(x, y, d)
    nx = x + dx[d]
    ny = y + dy[d]
    if world[nx][ny] == 0:
        x = nx
        y = ny
        world[x][y] = 2
        answer += 1
        count = 0
        continue
    else :
        count += 1
    if count == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if world[nx][ny] == 1:
            break
        else:
            x = nx
            y = ny
        count = 0

print(answer)
