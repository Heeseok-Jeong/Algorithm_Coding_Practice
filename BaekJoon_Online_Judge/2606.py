import sys
from collections import deque

def read_sys():
    return sys.stdin.readline()

def make_graph():
    graph_ = [[0 for _ in range(coms+1)] for _ in range(coms+1)]
    for x, y in info:
        graph_[x][y] = 1
        graph_[y][x] = 1
    return graph_

def bfs(start):
    visited = []
    que_ = deque()
    que_.append(start)
    while que_:
        x = que_.popleft()
        if x not in visited:
            if x != 1:
                visited.append(x)
            for i in range(2, coms+1):
                y = graph_[x][i]
                if y == 1 and i not in visited:
                    que_.append(i)
    return visited

coms = int(read_sys())
lines = int(read_sys())
info = [list(map(int, read_sys().split())) for _ in range(lines)]
graph_ = make_graph()
start = 1
visited = bfs(start)
result = len(visited)
print(result)
