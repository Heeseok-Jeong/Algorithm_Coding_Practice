def solve(n, m, depth):
    if depth == m:
        str_r = ""
        for i in result:
            str_r += str(i)
            str_r += " "
        print(str_r)
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            solve(n, m, depth+1)
            result.pop()
            visited[i] = False

n, m = map(int, input().split())
visited = [False] * (n+1)
result = []
depth = 0
solve(n, m, depth)
