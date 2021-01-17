n, m = map(int, input().split())
memo = [10001] * (m+1)
memo[0] = 0
currents = [int(input()) for _ in range(n)]

for current in currents:
    for i in range(current, m+1):
        if memo[i-current] != 10001:
            memo[i] = min(memo[i], memo[i-current] + 1)

if memo[m] == 10001:
    print(-1)
else:
    print(memo[m])
