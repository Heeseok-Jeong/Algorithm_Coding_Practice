import heapq
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
    print("target_index :", target_index)
    one_diff_list = []
    for i in range(len(total_words)):
        one_diff = {}
        for j in range(len(total_words)):
            count = 0
            for k in range(len(begin)):
                if total_words[i][k] != total_words[j][k]:
                    count += 1
            if count == 1:
                one_diff[j] = 1
        one_diff_list.append(one_diff)
    print("one_diff_list : {}".format(one_diff_list))

    shortest_diff = [INF] * len(total_words)
    start = 0
    pq = []
    diff = 0
    shortest_diff[start] = diff
    heapq.heappush(pq, [diff, start])

    while pq:
        prev_diff, start = heapq.heappop(pq)
        for to, diff in one_diff_list[start].items():
            new_diff = prev_diff + diff
            if shortest_diff[to] > new_diff:
                shortest_diff[to] = new_diff
                heapq.heappush(pq, [new_diff, to])

    print("shortest_diff :", shortest_diff)
    answer = shortest_diff[target_index]

    return answer
