import sys
from collections import deque
sys.setrecursionlimit(10**6)

def read_sys():
    return sys.stdin.readline()

def get_input(n_info):
    n_num, e_num, start = map(int, read_sys().split())
    for i in range(e_num):
        temp = list(map(int, read_sys().split()))
        n_list.append(temp)
    return n_num, e_num, start

def make_n_info(n_num, n_list, n_info):
    for a, b in n_list:
        n_info[a][b] = 1
        n_info[b][a] = 1

def DFS(start, n_info, visited):
    print(start, end=' ')
    visited[start] = True
    if False not in visited:
        return
    for i in range(1, len(visited)):
        if n_info[start][i] == 1 and visited[i] == False:
            DFS(i, n_info, visited)

def BFS(start, n_info, visited, dq):
    # 재귀
    # print(start, end=' ')
    # visited[start] = True
    # if False not in visited:
    #     return
    # for i in range(1, len(visited)):
    #     if n_info[start][i] == 1 and visited[i] == False:
    #         dq.append(i)
    # if dq:
    #     start = dq.leftpop()
    #     BFS(start, n_info, visited, dq)

    # 반복문
    dq.append(start)
    visited[start] = True
    result = ""
    while dq:
        node = dq.popleft()
        result += str(node)
        result += " "
        for i in range(1, len(visited)):
            if n_info[node][i] == 1 and visited[i] == False:
                visited[i] = True
                dq.append(i)
    print(result)

#main
n_list = []
n_num, e_num, start = get_input(n_list)
n_info = [[0] * (n_num+1) for row in range(n_num+1)]
make_n_info(n_num, n_list, n_info)
visited = [False]*(n_num+1)
visited[0] = True
DFS(start, n_info, visited)
print()
visited = [False]*(n_num+1)
visited[0] = True
dq = deque()
BFS(start, n_info, visited, dq)
