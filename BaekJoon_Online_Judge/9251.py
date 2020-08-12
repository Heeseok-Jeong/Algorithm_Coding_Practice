def solve():
    memo = [0 for _ in range(length)]
    temp = [0 for _ in range(length)]
    for i in range(len_1):
        a = alpha_1[i]
        if i == 0:
            for j in range(len_2):
                b = alpha_2[j]
                if a == b:
                    memo[j] += 1
                    temp[j] += 1
        else:
            for j in range(len_2):
                b = alpha_2[j]
                if a == b:
                    if j == 0:
                        temp[j] = 1
                    else:
                        temp[j] = max(memo[:j])+1
            memo = [i for i in temp]
    return memo

alpha_1 = input()
alpha_2 = input()
len_1 = len(alpha_1)
len_2 = len(alpha_2)
if len_1 > len_2:
    length = len_1
else:
    length = len_2
memo = solve()
result = max(memo)
print(result)
