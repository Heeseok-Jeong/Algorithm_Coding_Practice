import sys

def read_sys():
    return sys.stdin.readline()

def get_input(rgb_info):
    n = int(read_sys())
    for i in range(n):
        temp = list(map(int, read_sys().split()))
        rgb_info.append(temp)
    return n

def solve(n, rgb_info, result):
    for i in range(n):
        if i > 0:
            temp = [0 for j in range(3)]
            for j in range(3):
                for k in range(3):
                    if k != j:
                        if temp[j] == 0:
                            temp[j] = result[i-1][k] + rgb_info[i][j]
                        else:
                            if temp[j] > result[i-1][k] + rgb_info[i][j]:
                                temp[j] = result[i-1][k] + rgb_info[i][j]
            result[i] = temp

rgb_info = []
n = get_input(rgb_info)
result = rgb_info
solve(n, rgb_info, result)
print(min(result[n-1]))
