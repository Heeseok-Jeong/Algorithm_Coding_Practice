import sys
from collections import deque

def read_sys():
    return sys.stdin.readline()

def solve():
    result = 0
    while True:
        if queue[0][0] == max(queue)[0]:
            result += 1
            if queue[0][1] == 1:
                return result
            else:
                queue.popleft()
        else:
            queue.append(queue[0])
            queue.popleft()

size = int(read_sys())
for i in range(size):
    n, m = map(int, read_sys().split())
    info = deque(list(map(int, read_sys().split())))
    queue = deque()
    if n == 1:
        result = 1
    else:
        for j in range(n):
            a = info[j]
            if j == m:
                temp = [a, 1]
            else:
                temp = [a, 0]
            queue.append(temp)
        result = solve()
    print(result)
