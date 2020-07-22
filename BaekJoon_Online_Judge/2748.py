def fib_dp(n, memo):
    if memo[n] != -1: #값이 있으면 그냥 반환
        return memo[n]

    #메모한값 가져오기
    memo[n] = fib_dp(n-1, memo) + fib_dp(n-2, memo)
    return memo[n]

n = int(input())
memo = [-1]*(n+1)
memo[0] = 0
memo[1] = 1
print(fib_dp(n, memo))
