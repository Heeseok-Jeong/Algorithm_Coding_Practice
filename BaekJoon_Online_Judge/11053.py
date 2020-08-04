# #DFS로 풂 => 시간초과
# def solve(memo, index):
#     global result
#     count = len(memo)
#     count_2 = 0
#     last = memo[-1]
#     for i in range(index, len(n_list)):
#         n = n_list[i]
#         if last > n:
#             for j in range(len(memo)):
#                 n_2 = memo[j]
#                 if n_2 == n:
#                     break
#                 if n_2 > n:
#                     temp = memo[:j]
#                     temp.append(n)
#                     solve(temp, i+1)
#                     break
#
#         elif last < n:
#             last = n
#             memo.append(n)
#             count += 1
#     if result < count:
#         result = count
#
# n = int(input())
# n_list = list(map(int, input().split()))
# memo = []
# memo.append(n_list[0])
# index = 1
# result = 0
# solve(memo, index)
# print(result)

def solve():
    result = 0
    for i in range(1, length):
        n = n_list[i]
        temp = [1 for _ in range(i+1)]
        for j in range(i):
            m = n_list[j]
            if m < n:
                temp[j] = memo[j]
                temp[j] += 1
        memo[i] = max(temp)

    result = max(memo)
    return result

length = int(input())
n_list = list(map(int, input().split()))
memo = [1 for _ in range(length)]
result = solve()
print(result)
