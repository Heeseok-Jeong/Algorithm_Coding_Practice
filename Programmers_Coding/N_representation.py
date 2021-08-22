def solution(N, number):
    answer = 0
    memo = [-1] * 32000
    memo[0] = [0, [0]]
    count = 0
    count += 1
    memo[N] = [count, [5]]
    if N == number:
        return memo[N][0]
    
    q = [0]
    while q:
        count += 1
        n = q.pop()
        
        
    return answer