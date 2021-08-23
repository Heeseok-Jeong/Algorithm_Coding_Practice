def solution(triangle):
    answer = 0
    memo = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    memo[0][0] = triangle[0][0]
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])): 
            memo[i+1][j] = max(memo[i+1][j], memo[i][j]+triangle[i+1][j])
            memo[i+1][j+1] = max(memo[i+1][j+1], memo[i][j]+triangle[i+1][j+1])   
    answer = max(memo[len(memo)-1])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))