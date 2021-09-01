import heapq

INF = int(1e9)

def dijkstra(n, fares_arr, shortest, i):
    q = []
    heapq.heappush(q, (0, i))
    shortest[i][i] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        for j in range(1, n+1):
            if shortest[i][j] > shortest[i][now] + fares_arr[now][j]:
                shortest[i][j] = shortest[i][now] + fares_arr[now][j]
                heapq.heappush(q, (shortest[i][j], j))
                
def solution(n, s, a, b, fares):
    answer = int(INF)
    fares_arr = [[INF for _ in range(n+1)] for _ in range(n+1)]
    shortest = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for c, d, f in fares:
        fares_arr[c][d] = f
        fares_arr[d][c] = f
    
    for i in range(1, n+1):
        dijkstra(n, fares_arr, shortest, i)
    
    for i in range(1, n+1):
        answer = min(answer, shortest[s][i] + shortest[i][a] + shortest[i][b])
        
    return answer
