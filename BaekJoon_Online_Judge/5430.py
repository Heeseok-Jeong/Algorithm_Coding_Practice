from collections import deque
import sys

def read_sys():
    return sys.stdin.readline()

# def make_deq(temp):
#     temp.pop()
#     temp.popleft()
#     num_ = deque()
#     ele = ''
#     for n in temp:
#         if n == ',':
#             num_.append(int(ele))
#             ele = ''
#         else:
#             ele += n
#     num_.append(int(ele))
#     return num_

def solve(num_):
    len_ = len(num_)
    is_rvs = False
    if len_ < op_.count('D'):
        print('error')
        return
    for o in op_:
        if o == 'R':
            is_rvs = not is_rvs
        else:
            if not is_rvs:
                num_.popleft()
            else:
                num_.pop()
    num_ = list(num_)
    if not is_rvs:
        print(''.join(str(num_).split()))
    else:
        num_.reverse()
        print(''.join(str(num_).split()))

t = int(read_sys())
for _ in range(t):
    op_ = list(read_sys().strip())
    size = int(read_sys().strip())
    if size == 0:
        read_sys()
        num_ = deque()
    else:
        # num_ = make_deq(temp)
        num_ = deque(map(int, read_sys().strip()[1:-1].split(',')))
    # print(num_)
    solve(num_)
