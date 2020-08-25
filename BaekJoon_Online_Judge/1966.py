import sys
from collections import deque

def read_sys():
    return sys.stdin.readline()

def solve():
    for p in range(1, n):
        x = queue[p][0]
        for q in range(p-1, -1, -1):
            y = queue[q][0]
            print("p :", p, ", q :", q, ", x :", x, ", y :", y)
            if x >= y:
                temp = queue[p]
                queue[p] = queue[q]
                queue[q] = temp
                p = q
                print(queue)


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
        solve()
        for k in range(n):
            if queue[k][1] == 1:
                result = k+1
                break
    print(result)
