import sys

def read_sys():
    return sys.stdin.readline()

def get_input(num_list, op_list):
    size = int(read_sys())
    num_list = list(map(int, read_sys().split()))
    op_list = list(map(int, read_sys().split()))
    return size, num_list, op_list

def compute_division(sum,x):
    if sum < 0:
        temp = abs(sum)
        temp //= x
        return temp*-1
    else:
        return sum//x

#
def compute(size, num_list, op_list, result):
    sum = num_list[0]
    for i in range(1, size): 
        if op_list[i-1] == 0:
            sum += num_list[i]
        elif op_list[i-1] == 1:
            sum -= num_list[i]
        elif op_list[i-1] == 2:
            sum *= num_list[i]
        else:
            x = num_list[i]
            sum = compute_division(sum, x) #나눗셈은 - 있으면 C++처럼 해줌
    result.append(sum)

#재귀로 깊이 탐색, 연산자 중 1보다 큰 거 있으면 한 개만
def solve(size, depth, num_list, op_count, op_list, result): #숫자개수, 현재깊이, 숫자리스트, 연산자개수, 연산자리스트, 결과
    if depth==(size-1):
        compute(size, num_list, op_list, result)
        return
    for i in range(4):
        if op_count[i] >= 1:
            op_count[i] -= 1
            op_list.append(i)
            solve(size, depth+1, num_list, op_count, op_list, result)
            op_list.pop()
            op_count[i] += 1


def print_result(result):
    print(max(result))
    print(min(result))


size = 0
num_list = []
op_count = []
op_list = []
result = []
depth = 0
size, num_list, op_count = get_input(num_list, op_count) #인풋 사이즈, 숫자리스트, 연산자개수리스트 받음
solve(size, depth, num_list, op_count, op_list, result) #계산
print_result(result) #모든 연산 결과가 담긴 result에서 max와 min 프린트
