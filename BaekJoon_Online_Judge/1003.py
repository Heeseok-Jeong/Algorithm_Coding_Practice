import sys

def read_sys():
    return sys.stdin.readline()

#Recursion
# def fib(x, count_list):
#     if x == 0:
#         count_list[0] += 1
#         return 0
#     if x == 1:
#         count_list[1] += 1
#         return 1
#     return fib(x-1, count_list) + fib(x-2, count_list)
#
# n = int(read_sys())
# n_list = []
# for i in range(n): #입력 받기
#     n_list.append(int(read_sys()))
# for x in n_list: #각각 테스트 돌고 결과 출력
#     count_list = [0]*2
#     fib(x, count_list)
#     for i in count_list:
#         print(i, end=' ')
#     print()

#DP
def fib(x, count_list):
    if x==0:
        return count_list[0]
    if x==1:
        return count_list[1]
    if count_list[x] != [-1,-1]:
        return count_list[x]
    left = fib(x-1, count_list)
    right = fib(x-2, count_list)
    # print(x)
    # print(x-1, end=' : ')
    # print(left)
    # print(x-2, end=' : ')
    # print(right)
    count_list[x] = [left[0] + right[0], left[1] + right[1]]
    # count_list[x][0] = left[0] + right[0]
    # count_list[x][1] = left[1] + right[1]

    # print(count_list)
    return count_list[x]

n = int(read_sys())
n_list = []
count_zero = 0
count_one = 0
for i in range(n): #입력 받기
    n_list.append(int(read_sys()))
for x in n_list: #각각 테스트 돌고 결과 출력
    count_list = [[-1, -1]]*(x+2)
    count_list[0] = [1,0]
    count_list[1] = [0,1]
    result = fib(x, count_list)
    r_left = result[0]
    r_right = result[1]
    print(r_left, end=' ')
    print(r_right, end=' ')
    print()
