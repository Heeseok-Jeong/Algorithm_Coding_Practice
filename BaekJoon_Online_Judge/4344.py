import sys

n = int(sys.stdin.readline())
avg = 0

for i in range(1, n+1):
    num_list = list(map(int, sys.stdin.readline().split()))
    a = num_list[0]
    del num_list[0]

    avg = sum(num_list)/len(num_list)
    new_list = []
    for j in num_list:
        if j > avg:
            new_list.append(j)
    new_avg = 100*len(new_list)/a
    print(str('%.3f' % new_avg) + '%')
