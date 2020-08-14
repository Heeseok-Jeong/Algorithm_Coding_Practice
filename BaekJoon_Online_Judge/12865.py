def solve():
    for i in range(1, n+1):
        w = info[i][0]
        v = info[i][1]
        for j in range(1, k+1): #j : 최대무게
            if w > j:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = max(v + memo[i-1][j-w], memo[i-1][j])

n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
info.insert(0, [0,0])
memo = [[0 for _ in range(k+1)] for _ in range(n+1)]
solve()
result = memo[n][k]
print(result)
