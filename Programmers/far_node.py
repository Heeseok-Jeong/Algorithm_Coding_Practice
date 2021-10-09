from collections import deque

def solution(n, edge):
    answer = 0
    edges = [[] for _ in range(n+1)]
    for a, b in edge:
        edges[a].append(b)
        edges[b].append(a)
        
    shorts = [1e9 for _ in range(n+1)]   
    visited = [0 for _ in range(n+1)]   
    dq = deque()
    dq.append(1)
    shorts[1] = 0
    while dq:
        now = dq.popleft()
        visited[now] = 1
        for i in edges[now]:
            if shorts[i] > shorts[now] + 1:
                shorts[i] = shorts[now] + 1
                dq.append(i)
    
    shorts = shorts[1:]
    max_num = max(shorts)
    for n in shorts:
        if n == max_num:
            answer += 1
    
    return answer
