from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * n
    dq = deque()

    i = 0
    while False in visited:
        if not visited[i]:
            x = i
            visited[x] = True
            for j in range(n):
                if computers[x][j] and not visited[j]:
                    dq.append(j)
            while dq:
                x = dq.popleft()
                visited[x] = True
                for j in range(n):
                    if computers[x][j] and not visited[j]:
                        dq.append(j)
            answer += 1
        i += 1

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
answer = solution(n, computers)
print(answer)
