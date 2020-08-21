import sys
from collections import deque

def read_sys():
    return sys.stdin.readline()

def solve(str_):
    if len(str_) == 2:
        queue.append(str_[1])
    else:
        str_ = str_[0]
        if str_ == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif str_ == "size":
            print(len(queue))
        elif str_ == "empty":
            if queue:
                print(0)
            else:
                print(1)
        elif str_ == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif str_ == "back":
            if queue:
                print(queue[len(queue)-1])
            else:
                print(-1)


n = int(read_sys())
queue = deque()
for i in range(n):
    str_ = list(read_sys().split())
    solve(str_)
