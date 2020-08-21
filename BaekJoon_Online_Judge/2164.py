from collections import deque

def solve():
    queue = deque(i for i in range(n, 0, -1))
    for i in range(n):
        if len(queue) == 1:
            print(queue[0])
            return
        queue.pop()
        x = queue.pop()
        queue.appendleft(x)


n = int(input())
solve()
