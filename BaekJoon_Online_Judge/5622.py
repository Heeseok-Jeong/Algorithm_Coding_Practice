import sys

def convert_num(a):
    x = 0
    a_num = ord(a)
    for i in range(0, 8):
        if i < 5:
            for j in range(0, 3):
                if 65+j+3*i == a_num:
                    x = i
        elif i == 5:
            for j in range(0, 4):
                if 65+j+3*5 == a_num:
                    x = i
        elif i == 6:
            for j in range(0, 3):
                if 65+j+3*6+1 == a_num:
                    x = i
        else:
            for j in range(0, 4):
                if 65+j+3*7+1 == a_num:
                    x = i
    x += 2
    return x

a_str = sys.stdin.readline().strip()

n_list = []
for i in a_str:
    n_list.append(convert_num(i))

print(sum(n_list)+len(n_list))
