import sys
from collections import deque

input = sys.stdin.readline

DEAD, EMPTY, APPLE, BODY = -1, 0, 1, 2

def turn_head(d, message):
    if message == "L":
        d -= 1
        if d < 0:
            d = 3
    elif message == "D":
        d += 1
        if d > 3:
            d = 0
    return d

N = int(input())
grid = [[DEAD] * (N+1)]
grid += [([DEAD] + [EMPTY]*N + [DEAD]) for _ in range(N)]
grid += [[DEAD] * (N+1)]
grid[1][1] = BODY

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    grid[x][y] = APPLE

L = int(input())
changes = deque()
for _ in range(L):
    reserved_time, message = input().split()
    changes.append((int(reserved_time), message))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1
t = 0
r_t, m = changes.popleft()
body = deque([[1, 1]])

while True:
    # move
    x, y = body[-1]
    new_x, new_y = x+dx[d], y+dy[d]
    t += 1

    # dead check
    if grid[new_x][new_y] in [DEAD, BODY]:
        break

    # set new state
    body.append([new_x, new_y])
    if grid[new_x][new_y] != APPLE:
        p_x, p_y = body.popleft()
        grid[p_x][p_y] = EMPTY
    grid[new_x][new_y] = BODY

    # turn check
    if r_t == t:
        d = turn_head(d, m)
        if changes:
            r_t, m = changes.popleft()
    
print(t)
