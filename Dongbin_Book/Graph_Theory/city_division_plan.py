import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    p_a = find_parent(parent, a)
    p_b = find_parent(parent, b)

    if p_a < p_b:
        parent[p_b] = p_a
    elif p_a > p_b:
        parent[p_a] = p_b

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
parent = [i for i in range(n+1)]

total_cost = 0
max_cost = 0
used_edges = []
for c, a, b in edges:
    if a > b:
        a, b = b, a
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += c
        used_edges.append((c, a, b))
        max_cost = c

answer = total_cost - max_cost
print(answer)
