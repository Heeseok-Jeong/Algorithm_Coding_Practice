n = int(input())
foods = list(map(int, input().split()))
memo = [0 for _ in range(n)]
memo[0], memo[1] = foods[0], max(foods[0], foods[1])

for i in range(2, n):
    memo[i] = max(memo[i-1], foods[i] + memo[i-2])

print(memo[n-1])
