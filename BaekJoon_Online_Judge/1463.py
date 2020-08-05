def solve():
    for i in range(4, n+1):
        temp = []
        if i%3 == 0:
            temp.append(memo[i//3]+1)
        if i%2 == 0:
            temp.append(memo[i//2]+1)
        temp.append(memo[i-1]+1)
        memo[i] = min(temp)
        # print("i :", i, ", temp :", temp, ", memo :", memo)

n = int(input())
if n == 1:
    print(0)
elif n == 2:
    print(1)
elif n == 3:
    print(1)
else:
    memo = [0 for _ in range(n+1)]
    memo[2] = 1
    memo[3] = 1
    solve()
    result = memo[n]
    print(result)
