def solve():
# 반례, 거꾸로 찾으면 안될듯 순서대로 찾자
# 5
# 50
# 40
# 30
# 20
# 10
    result = n_list[length-1]
    memo.append(n_list[length-1])
    count = 1
    for i in range(length-1, 0, -1):
        print(i, ",", memo, ", count :", count, ", i-1 :", n_list[i-1], ", i-2 :", n_list[i-2])
        if count == 2:
            count = 0
            continue
        if i == 1:
            memo.append(n_list[i-1])
            result += n_list[i-1]

        elif n_list[i-1] >= n_list[i-2]:
            count += 1
            memo.append(n_list[i-1])
            result += n_list[i-1]
        else:
            count = 2
            memo.append(n_list[i-2])
            result += n_list[i-2]

    return result

length = int(input())
n_list = [int(input()) for _ in range(length)]
# memo = [0 for _ in range(length)]
memo = []
result = solve()
print(result)
