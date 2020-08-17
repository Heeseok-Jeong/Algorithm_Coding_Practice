import sys

def solve():
    global top
    if "push" in str:
        _, x = str.split()
        stack.append(x)
        top += 1
    elif "pop" in str:
        if top == -1:
            print(-1)
            return
        x = stack[top]
        del stack[top]
        top -= 1
        print(x)
    elif "size" in str:
        size = top + 1
        print(size)
    elif "empty" in str:
        if top == -1:
            print(1)
        else:
            print(0)
    elif "top" in str:
        if top == -1:
            print(-1)
        else:
            x = stack[top]
            print(x)

n = int(sys.stdin.readline())
stack = []
top = -1
for i in range(n):
    str = sys.stdin.readline()
    solve()
