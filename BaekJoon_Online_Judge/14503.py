import sys

n, m = map(int, input().split())
r, c, d = map(int, input().split())
field = []
for i in range(n):
    field.append(list(map(int, input().split())))

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
count = 0
stack = [[r, c]]

while stack:
    r, c = stack.pop()
    if field[r][c] == 0:
        field[r][c] = 2
        count += 1
    temp_d = d
    back = True
    for i in range(4):
        temp_d -= 1
        if temp_d == -1:
            temp_d = 3

        nr = r+dr[temp_d]
        nc = c+dc[temp_d]
        if nr < 0 or nr > n-1 or nc < 0 or nc > m-1:
            continue
        if field[nr][nc] != 0:
            continue
        else:
            d = temp_d
            stack.append([nr, nc])
            back = False
            break
    if back:
        nr = r-dr[temp_d]
        nc = c-dc[temp_d]
        if field[nr][nc] == 1 or nr < 0 or nr > n-1 or nc < 0 or nc > m-1:
            break
        else:
            stack.append([nr, nc])

print(count)
