import sys

n = int(sys.stdin.readline())
x = int(sys.stdin.readline())
temp = x
x_list = [0] * n

for i in range(n-1, -1, -1):
    x_list[i] = temp%10
    temp //= 10


print(sum(x_list))
