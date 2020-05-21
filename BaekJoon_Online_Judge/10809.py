import sys

a = sys.stdin.readline()
x_list = [-1] * 26
count = 0
result = ""

for i in a:
    for j in range(97, 123):
        k = j-97
        if i == chr(j) and x_list[k] == -1:
            x_list[k] = count
    count += 1

for i in x_list:
    result += str(i)
    result += " "
print(result)
