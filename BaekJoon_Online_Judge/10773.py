import sys

def read_sys():
    return sys.stdin.readline()

n = int(read_sys())
stack = []
for i in range(n):
    x = int(read_sys())
    if x == 0:
        if stack:
            stack.pop()
    else:
        stack.append(x)
result = sum(stack)
print(result)
