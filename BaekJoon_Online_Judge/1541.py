def split_input(str_input, num_list, op_list):
    temp = ''
    for i in str_input:
        if i == '+':
            num_list.append(int(temp))
            op_list.append(i)
            temp = ''
        elif i == '-':
            num_list.append(int(temp))
            op_list.append(i)
            temp = ''
        else:
            temp += i
    num_list.append(int(temp))

def solve(str_input, num_list, op_list):
    min = 0
    for i in range(len(num_list)):
        if i == 0:
            min = num_list[i]
        else:
            # print(op_list[i-1])
            if op_list[i-1] == '+':
                min += num_list[i]
            elif op_list[i-1] == '-' and op_list[i] == -1:
                # print(2)
                # print(num_list[i])
                min -= num_list[i]
            elif op_list[i-1] == '-' and op_list[i] == '-':
                # print(2)
                # print(num_list[i])
                min -= num_list[i]
            elif op_list[i] == -1:
                break
            else:
                # print(3)
                min = min - num_list[i] - 2*num_list[i+1]
        # print(i, ":", min)
    return min

str_input = input()
num_list = []
op_list = []
split_input(str_input, num_list, op_list)
op_list.append(-1)
# print(num_list)
# print(op_list)
print(solve(str_input, num_list, op_list))
