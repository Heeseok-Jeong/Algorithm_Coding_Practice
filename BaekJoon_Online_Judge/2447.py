def solve(n, x, y): #9
    if n == 3:
        for i in range(x, x+3):
            for j in range(y, y+3):
                if not (i%3 == 1 and j%3 == 1):
                    star[i][j] = '*'
        return#9,0,9
    for i in range(x, x+n, n//3): #0, 3, 6
        for j in range(y, y+n, n//3): #9, 12, 15
            if not (i-x == n//3 and j-y == n//3): #3,12 일때 막아야 함
                solve(n//3, i, j)

n = int(input())
star = [[" " for _ in range(n)] for _ in range(n)]
x, y = 0, 0
solve(n, x, y)
for i in range(n):
    for j in range(n):
        print(star[i][j], end='')
    print()
