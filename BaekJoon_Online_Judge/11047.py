import sys

def read_sys():
    return sys.stdin.readline()

def get_input(n_list):
    n, k = map(int, read_sys().split())
    for i in range(n):
        n_list.append(int(read_sys()))
    return n, k

def solve(n, k, n_list):
    count = 0
    temp = k
    new_list = n_list
    new_list.reverse()
    for i in new_list:
        if temp < i:
            continue
        count += (temp//i)
        temp %= i
    return count

n_list = []
n, k = get_input(n_list)
count = solve(n, k, n_list)
print(count)
