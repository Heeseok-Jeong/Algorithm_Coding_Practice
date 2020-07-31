import sys

def read_sys():
    return sys.stdin.readline()

def solve():
    count = 0
    time = 0
    for x, y in time_list:
        if time <= x:
            time = y
            count += 1
    return count

n = int(read_sys())
time_list = [list(map(int, read_sys().split())) for _ in range(n)]
time_list = sorted(time_list, key = lambda x : (x[1], x[0]))
print(solve())
