import sys

def read_sys():
    return sys.stdin.readline()

def solve():
    temp = 0
    for i in range(size):
        n = n_list[i]
        flag = False
        while not flag:
            if temp == n:
                stack.pop()
                result.append("-")
                flag = True
            elif temp > n:
                if n == stack[len(stack)-1]:
                    stack.pop()
                    result.append("-")
                    flag = True
                elif not stack:
                    print("check")
                    for x in result:
                        print(x)
                    return
                else:
                    print("NO")
                    return
            else:
                temp += 1
                stack.append(temp)
                result.append("+")
    for x in result:
        print(x)

size = int(read_sys())
stack = []
result = []
n_list = [int(read_sys()) for _ in range(size)]
solve()
