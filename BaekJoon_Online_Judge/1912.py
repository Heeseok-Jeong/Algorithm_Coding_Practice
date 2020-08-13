def check_only_neg():
    flag = 1
    for n in n_list:
        if n > 0:
            flag = 0
            break
    return flag

def minimize():
    temp_p = 0
    temp_n = 0
    new_list = []
    for n in n_list:
        if n == 0:
            continue
        if n < 0:
            if temp_p != 0:
                new_list.append(temp_p)
            temp_p = 0
            temp_n += n
        else:
            if temp_n != 0:
                new_list.append(temp_n)
            temp_n = 0
            temp_p += n
    if temp_p != 0:
        new_list.append(temp_p)
    if temp_n != 0:
        new_list.append(temp_n)
    return new_list

def solve():
    for i in range(length):
        n = n_list[i]
        if i == 0:
            memo[i] = n
        else:
            if n < 0:
                memo[i] = memo[i-1] + n
            else:
                if memo[i-1] + n > n:
                    memo[i] = memo[i-1] + n
                else:
                    memo[i] = n

length = int(input())
n_list = list(map(int, input().split()))
if check_only_neg():
    result = max(n_list)
else:
    n_list = minimize()
    length = len(n_list)
    memo = [0 for _ in range(length)]
    solve()
    result = max(memo)
print(result)
