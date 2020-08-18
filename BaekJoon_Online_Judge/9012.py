import sys

def read_sys():
    return sys.stdin.readline()

def solve():
    if str[0] == ')':
        stack.append(0)
    else:
        for i in range(len(str)):
            x = str[i]
            stack.append(x)
            if stack[0] == ')':
                return
            if stack[len(stack)-1] == ')':
                stack.pop()
                stack.pop()

size = int(read_sys())
for _ in range(size):
    stack = []
    result = "NO"
    str = (read_sys()).split()
    str = str[0]
    solve()
    if len(stack) == 0:
        result = "YES"
    print(result)
