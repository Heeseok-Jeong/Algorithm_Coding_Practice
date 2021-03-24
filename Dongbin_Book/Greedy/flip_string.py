init = input()

arr = [int(init[0])]
for i in range(1, len(init)):
    if init[i-1] != init[i]:
        arr.append(int(init[i]))

count_zero = 0
count_one = 0
for x in arr:
    if x == 0:
        count_zero += 1
    else:
        count_one += 1

print(min(count_zero, count_one))
