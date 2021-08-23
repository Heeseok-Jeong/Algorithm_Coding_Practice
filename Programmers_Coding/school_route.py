from collections import deque

def solution(m, n, puddles):
    answer = 0
    grid = [[0 for _ in range(m+1)] for _ in range(n+1)]
    grid[1][0] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] not in puddles:
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
    answer = grid[n][m] % 1000000007
    return answer

print(solution(4, 3, [[2, 2]]))
