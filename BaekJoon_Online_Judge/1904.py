# 반복문 + DP, 결과에 계속 15746 나눠야 시간 오래 안걸림
def solve(n):
    if n == 1:
        return 1
    else:
        v0, v1 = 1, 1
        for i in range(2, n+1):
            v2 = (v0 + v1)%15746
            v0, v1 = v1, v2
        return v2
            # result[i] = result[i-1] + result[i-2]
            # result.append(result[i-1] + result[i-2])
        # print(result)
        
n = int(input())
# result = [1 for i in range(n+1)]
result = [1, 1]
# print("len : ", len(result))
# solve(n, result)
print(solve(n))



# 재귀 + DP => 런타임 에러
# def solve(n, result):
#     if result[n] != -1:
#         return result[n]
#     result[n] = (solve(n-1, result) + solve(n-2, result)) % 15746
#     return result[n]
#
# def print_result(n, result):
#     print(result[n] % 15746)
#
# n = int(input())
# result = [-1 for i in range(n+1)]
# result[0] = 1
# result[1] = 1
# print(solve(n, result))
# print_result(n, result)
