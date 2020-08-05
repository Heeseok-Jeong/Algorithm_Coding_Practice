def solve():
    return

length = int(input())
s_list = [int(input()) for _ in range(length)]
memo = [0 for _ in range(length)]
memo[0] = s_list[0]
if length == 1:
    print(s_list[0])
elif length == 2:
    print(s_list[0] + s_list[1])
else:
    memo[1] = s_list[0] + s_list[1]
    memo[2] = max(s_list[0]+s_list[2], s_list[1]+s_list[2])
    for i in range(3, length):
        memo[i] = max(memo[i-3]+s_list[i-1]+s_list[i], memo[i-2]+s_list[i])
    print(memo[length-1])
