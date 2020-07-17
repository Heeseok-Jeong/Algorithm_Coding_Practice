import sys

def read_sys():
    return sys.stdin.readline()

def get_input(n_info):
    n_num, e_num, start = int(read_sys().split())
    for i in range(e_num):
        temp = list(map(int, read_sys.split()))
        n_info.append(temp)
        return n_num, e_num

n_info = []
n_num, e_num = get_input(n_info)
visited = [False]*(n_num+1)
print(n_num)
print(e_num)
print(n_info)
