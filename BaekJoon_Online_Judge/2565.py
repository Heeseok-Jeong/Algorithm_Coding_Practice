def solve():
    for i in range(1, length):
        temp = 1
        left, right = info_list[i]
        for j in range(i):
            temp_l, temp_r = info_list[j]
            if (left > temp_l and right > temp_r) and (temp < memo[j]+1):
                temp = memo[j] + 1
        memo[i] = temp

length = int(input())
info_list = [list(map(int, input().split())) for _ in range(length)]
info_list = sorted(info_list)
memo = [1 for _ in range(length)]
if length == 1:
    result = 0
else:
    solve()
    result = length - max(memo)
print(result)
