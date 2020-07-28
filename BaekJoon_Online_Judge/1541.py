# def split_input(str_input, num_list, op_list):
#     temp = ''
#     for i in str_input:
#         if i == '+':
#             num_list.append(int(temp))
#             op_list.append(i)
#             temp = ''
#         elif i == '-':
#             num_list.append(int(temp))
#             op_list.append(i)
#             temp = ''
#         else:
#             temp += i
#     num_list.append(int(temp))
#
# def solve(str_input, num_list, op_list):
#     min = 0
#     flag = 0
#     temp = 0
#     for i in range(len(num_list)):
#         if i == 0:
#             min = num_list[i]
#         else:
#             if op_list[i-1] == '+':
#                 min += num_list[i]
#             elif op_list[i-1] == '-':
#                 temp += num_list[i]
#                 flag = 1
#             # elif op_list[i-1] == '-' and op_list[i] == -1:
#             #     min -= num_list[i]
#             # elif op_list[i-1] == '-' and op_list[i] == '-':
#             #     min -= num_list[i]
#             # elif op_list[i] == -1:
#             #     break
#             # else:
#             #     min = min - num_list[i] - 2*num_list[i+1]
#     return min
#
# str_input = input()
# num_list = []
# op_list = []
# split_input(str_input, num_list, op_list)
# op_list.append(-1)
# # print(num_list)
# # print(op_list)
# print(solve(str_input, num_list, op_list))

#1. 인풋은 2-3+3+3-1 이런식이므로 첫 숫자만 더하고 뒤에는 -부터 -사이 값들을 더하여 -해줌
#2. split('-')함. 2, 3+3+3, 1로 분리됨
#3. 처음은 더하고 나머지는 split('+')로 분리해서 뺌
removed_minus_list = input().split('-')
min = 0
for i in range(len(removed_minus_list)):
    if i == 0:
        if removed_minus_list[i].find('+') == -1:
            min += int(removed_minus_list[i])
        else:
            temp = map(int, removed_minus_list[i].split('+'))
            min += sum(temp)
    else:
        if removed_minus_list[i].find('+') == -1:
            min -= int(removed_minus_list[i])
        else:
            temp = map(int, removed_minus_list[i].split('+'))
            min -= sum(temp)
print(min)
