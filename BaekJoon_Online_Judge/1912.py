def minimize():
    temp = 0
    new_list = []
    for n in n_list:
        if n == 0:
            continue
        if n < 0:
            if temp != 0:
                new_list.append(temp)
            temp = 0
            new_list.append(n)
        else:
            temp += n
    if temp != 0:
        new_list.append(temp)
    return new_list

def solve():
    return

length = int(input())
n_list = list(map(int, input().split()))
n_list = minimize()
