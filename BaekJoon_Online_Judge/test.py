import sys

def read_sys():
    return sys.stdin.readline()

def solve():
    time = 0
    count = 0
    for x, y in sorted_time_list:
        if time <= x:
            time = y
            count += 1
    return count

n = int(read_sys())
time_list = [list(map(int, read_sys().split())) for _ in range(n)]
sorted_time_list = sorted(time_list, key = lambda x : (x[1], x[0]))
print(time_list)
print(sorted_time_list)
count = solve()
print(count)
