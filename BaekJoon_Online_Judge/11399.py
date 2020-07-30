def solve():
    min = 0
    time_list.sort()
    for i in range(1, n):
        time_list[i] += time_list[i-1]

    min = sum(time_list)
    return min

n = int(input())
time_list = list(map(int, input().split()))
print(solve())
