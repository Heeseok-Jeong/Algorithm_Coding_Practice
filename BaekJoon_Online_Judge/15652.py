from collections import deque

def solve(depth):
    if depth == m:
        print(*result)
        return

    for i in range(1, n+1):
        if not visited[i]:
            for j in range(i):
                visited[j] = True
            result.append(i)
            solve(depth+1)
            result.pop()
            for j in range(i):
                visited[j] = False

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
result = deque()
depth = 0
solve(depth)
