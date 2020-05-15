import sys

num_list = []

for i in range(1, 11):
    a = int(sys.stdin.readline()) % 42
    state = 0

    if not num_list:
        num_list.append(a)
    else:
        for j in num_list:
            if a == j:
                state = 1
        if state == 0:
            num_list.append(a)

print(len(num_list))
