from collections import deque
import pprint

n = int(input())
indegree = [0] * (n+1)
spending_time = [0] * (n+1)
needed_time = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    user_input = list(map(int, input().split()))
    spending_time[i] = user_input[0]
    needed_time[i] = user_input[0]
    indegree[i] += len(user_input) - 2
    for to in user_input[1:-1]:
        graph[to].append(i)

# pprint.pprint(f"indegree : {indegree}")
# pprint.pprint(f"graph")
# pprint.pprint(graph)
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for to in graph[now]:
        indegree[to] -= 1
        needed_time[to] = max(needed_time[now], needed_time[now] + spending_time[to])
        if indegree[to] == 0:
            q.append(to)
            

for i in range(1, n+1):
    print(needed_time[i])
