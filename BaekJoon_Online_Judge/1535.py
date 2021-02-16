n = int(input())
L = [0] + list(map(int, input().split()))
J = [0] + list(map(int, input().split()))

memo = [[0 for _ in range(101)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, 101):
        memo[i][j] = memo[i-1][j]
        if j-L[i] > 0:
            memo[i][j] = max(memo[i][j], memo[i-1][j-L[i]] + J[i])

print(memo[n][100])
