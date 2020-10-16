import sys

str_a, str_b = sys.stdin.readline().split()

len_a = len(str_a)
len_b = len(str_b)

count_min = len_a

for i in range(0, len_b-len_a+1):
    count_i = 0
    for j in range(0, len_a):
        if str_a[j] != str_b[j+i]:
            count_i += 1
    if count_min > count_i:
        count_min = count_i

print(count_min)
