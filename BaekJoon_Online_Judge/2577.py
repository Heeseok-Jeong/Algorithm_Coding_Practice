import sys

count_list = [0]*10

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

x = str(a*b*c)

for i in x:
    if i == '0':
        count_list[0] += 1
    elif i == '1':
        count_list[1] += 1
    elif i == '2':
        count_list[2] += 1
    elif i == '3':
        count_list[3] += 1
    elif i == '4':
        count_list[4] += 1
    elif i == '5':
        count_list[5] += 1
    elif i == '6':
        count_list[6] += 1
    elif i == '7':
        count_list[7] += 1
    elif i == '8':
        count_list[8] += 1
    elif i == '9':
        count_list[9] += 1

for i in count_list:
    print(i)
