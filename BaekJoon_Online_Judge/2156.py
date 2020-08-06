def solve():
    for i in range(1, n+1):
        if i == 1:
            memo[i] = n_list[i]
        elif i == 2:
            memo[i] = n_list[i-1] + n_list[i]
        elif i == 3:
            temp = max(n_list[i-2]+n_list[i], n_list[i-1]+n_list[i])
            temp = max(temp, memo[i-1])
            memo[i] = temp
        else:
            temp = max(memo[i-2]+n_list[i], memo[i-3]+n_list[i-1]+n_list[i])
            temp = max(temp, memo[i-1])
            memo[i] = temp

n = int(input())
n_list = [0 for _ in range(n+1)]
for i in range(1, n+1):
    n_list[i] = int(input())
memo = [0 for _ in range(n+1)]
solve()
result = memo[n]
print(result)
