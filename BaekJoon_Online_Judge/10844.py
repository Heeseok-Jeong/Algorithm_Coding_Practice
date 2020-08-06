def solve():
    for i in range(1, n+1):
        if i == 1:
            for j in range(1, 10):
                memo[i][j] = 1
        else:
            for j in range(10):
                if j == 0:
                    memo[i][j] = memo[i-1][j+1]
                elif j == 9:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = (memo[i-1][j-1] + memo[i-1][j+1]) % (10**9)

n = int(input())
memo = [[0 for _ in range(11)] for _ in range(n+1)]
solve()
result = sum(memo[n])%(10**9)
print(result)

#원소 다 구하는 방식 => 메모리 초과
# def solve():
#     for i in range(1, n+1):
#         temp = []
#         if i == 1:
#             for j in range(1, 10):
#                 temp.append(j)
#         else:
#             for j in memo[i-1]:
#                 if j%10 == 0:
#                     value = j*10 + 1
#                     temp.append(value)
#                 elif j%10 == 9:
#                     value = j*10 + 8
#                     temp.append(value)
#                 else:
#                     value = j*10 + (j%10 + 1)
#                     temp.append(value)
#                     value = j*10 + (j%10 -1)
#                     temp.append(value)
#         memo.append(temp)
#
# n = int(input())
# memo = [[]]
# solve()
# # print(memo)
# result = len(memo[n])%(10**9)
# print(result)
