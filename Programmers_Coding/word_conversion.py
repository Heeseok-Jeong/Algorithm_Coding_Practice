from collections import deque
import sys

INF = sys.maxsize

def solution(begin, target, words):
    answer = 0
    total_words = []
    total_words.append(begin)
    total_words.extend(words)

    if target not in words:
        return 0

    target_index = words.index(target)+1
    len_total = len(total_words)
    one_diff_matrix = [[0 for _ in range(len_total)] for _ in range(len_total)]

    for i in range(len_total):
        for j in range(len_total):
            count = 0
            for k in range(len(begin)):
                if total_words[i][k] != total_words[j][k]:
                    count += 1
            if count == 1:
                one_diff_matrix[i][j] = 1

    print(one_diff_matrix)

    dq = deque()
    min_diff = [INF] * len_total
    visited = [False] * len_total
    start = 0
    min_diff[start] = 0
    diff = min_diff[start]
    visited[start] = True
    for i in range(len_total):
        if one_diff_matrix[start][i] == 1:
            dq.append(i)
            if min_diff[i] > min_diff[start]+1 :
                min_diff[i] = min_diff[start]+1

    while dq:
        start = dq.popleft()
        diff = min_diff[start]
        visited[start] = True
        for i in range(len_total):
            if one_diff_matrix[start][i] == 1 and not visited[i]:
                dq.append(i)
                if min_diff[i] > min_diff[start]+1 :
                    min_diff[i] = min_diff[start]+1

    print("min_diff :", min_diff)
    answer = min_diff[target_index]
    return answer

begin = "hit"
target = "cog"
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
answer = solution(begin, target, words)
print(answer)
