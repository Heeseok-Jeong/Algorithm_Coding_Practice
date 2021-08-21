import sys 

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    scores = []
    scores.append(list(map(int, input().split())))
    scores.append(list(map(int, input().split())))

    if n == 1:
        result = max(scores[0][0], scores[1][0])
    else:
        memo = [[0 for _ in range(n)] for _ in range(2)]
        memo[0][0], memo[1][0] = scores[0][0], scores[1][0]
        memo[0][1] = memo[1][0] + scores[0][1]
        memo[1][1] = memo[0][0] + scores[1][1]

        for i in range(2, n):
            max_num_i_minus_2th = max(memo[0][i-2], memo[1][i-2])
            v_0 = max(max_num_i_minus_2th, memo[1][i-1]) + scores[0][i]
            memo[0][i] = v_0

            v_1 = max(max_num_i_minus_2th, memo[0][i-1]) + scores[1][i]
            memo[1][i] = v_1

        result = max(max(memo[0]), max(memo[1]))
    print(result)
