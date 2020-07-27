import sys

def read_sys():
    return sys.stdin.readline()

def get_input(n_list):
    n = int(read_sys())
    for i in range(n):
        n_list.append(int(read_sys()))

def solve(n, memo):
    for i in range(n):
        if i < 3:
            memo[i] = 1
        elif i == 4:
            memo[i] = 2
        elif i < 8:
            memo[i] = memo[i-1] + 1
        else:
            memo[i] = memo[i-1] + memo[i-5]

n_list = []
get_input(n_list)
for i in n_list:
    memo = [-1 for j in range(i)]
    solve(i, memo)
    print(memo[i-1])
