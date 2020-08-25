import sys
from collections import deque

def read_sys():
    return sys.stdin.readline()

def solve(str_):
    if len(str_) == 2:
        if str_[0] == 'push_front':
            deq_.appendleft(str_[1])
        else:
            deq_.append(str_[1])
    else:
        str_ = str_[0]
        if str_ == 'pop_front':
            if len(deq_) == 0:
                print(-1)
            else:
                print(deq_.popleft())
        elif str_ == 'pop_back':
            if len(deq_) == 0:
                print(-1)
            else:
                print(deq_.pop())
        elif str_ == 'size':
            print(len(deq_))
        elif str_ == 'empty':
            if len(deq_) == 0:
                print(1)
            else:
                print(0)
        elif str_ == 'front':
            if len(deq_) == 0:
                print(-1)
            else:
                print(deq_[0])
        elif str_ == 'back':
            if len(deq_) == 0:
                print(-1)
            else:
                print(deq_[len(deq_)-1])

size = int(read_sys())
deq_ = deque()
for _ in range(size):
    str_ = read_sys().split()
    solve(str_)
