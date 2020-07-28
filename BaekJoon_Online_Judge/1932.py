import sys

def read_sys():
    return sys.stdin.readline()

def get_input(n_list):
    n = int(read_sys())
    for i in range(n):
        n_list.append(list(map(int, read_sys().split())))
    return n

def solve(n_list, result):
    for i in range(len(n_list)): #i : depth, start from 0 to n-1
        if i > 0:
            temp = [0 for j in range(i+1)]
            for j in range(i):
                if temp[j] < n_list[i][j] + result[i-1][j]:
                    temp[j] = n_list[i][j] + result[i-1][j]
                if temp[j+1] < n_list[i][j+1] + result[i-1][j]:
                    temp[j+1] = n_list[i][j+1] + result[i-1][j]
            result[i] = temp

n_list = []
n = get_input(n_list)
result = n_list
solve(n_list, result)
print(max(result[n-1]))
