n = int(input())
memo = [0 for _ in range(n+1)]
memo[1] = 1
memo[2] = 3

for i in range(3, n+1):
    memo[i] = (memo[i-1] + 2*memo[i-2]) % 796796

print(memo[i])
