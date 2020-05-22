import sys

count = 0
x_list = sys.stdin.readline().strip()

for i in x_list:
    if i == ' ':
        count += 1

if x_list == '':
    print(0)
else:
    print(count+1)
