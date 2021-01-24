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
        parent[b] = p_a
    elif p_a > p_b:
        parent[a] = p_b

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]

user_inputs = [(map(int, input().rstrip().split())) for _ in range(m)]

for command, a, b in user_inputs:
    if command == 0:
        union_parent(parent, a, b)
    elif command == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
