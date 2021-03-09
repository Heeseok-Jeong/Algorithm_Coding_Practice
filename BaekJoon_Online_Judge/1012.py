import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

T = int(input())

def move_bug(grid, a, b):
    if grid[a][b] == 1:
        grid[a][b] = 0
        move_bug(grid, a+1, b)
        move_bug(grid, a-1, b)
        move_bug(grid, a, b+1)
        move_bug(grid, a, b-1)
        return 1
    return 0

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0 for _ in range(M+2)] for _ in range(N+2)]
    cabbages = []
    for i in range(K):
        X, Y = map(int, input().split())
        X, Y = X+1, Y+1
        grid[Y][X] = 1
        cabbages.append((Y, X))
    
    result = 0
    for a, b in cabbages:
        result += move_bug(grid, a, b)

    print(result)
