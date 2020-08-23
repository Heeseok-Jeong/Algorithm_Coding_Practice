from collections import deque

def solve():
    # queue = deque(i for i in range(1, n+1))
    queue = [i for i in range(1, n+1)]
    temp = []
    index = 0
    for i in range(n):
        if len(queue) == 1:
            temp.append(str(queue[0]))
        else:
            

n, k = map(int, input().split())
solve()
result = '<'
result += ', '.join(temp)
result += '>'
print(result)
