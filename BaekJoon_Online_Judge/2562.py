import sys

num_list = []
max = 0
max_idx = 0

for i in range(1, 10):
    a = int(sys.stdin.readline())
    if max < a:
        max = a
        max_idx = i

print(max)
print(max_idx)
