from collections import deque
import copy

def browse(x, target_index, visited, one_diff_list, stack, count, answer):
    if x == target_index:


def solution(begin, target, words):
    answer = 0
    word_length = len(begin)
    total_words = copy.deepcopy(words)
    total_words.insert(0, begin)
    total_words.append(target)
    total_words_size = len(total_words)
    one_diff_list = {}
    dq = deque()

    if target in words:
        for i in range(total_words_size):
            one_diff = []
            for j in range(i, total_words_size):
                count = 0
                for k in range(word_length):
                    if total_words[i][k] != total_words[j][k]:
                        count += 1
                if count == 1:
                    one_diff.append(j)
            one_diff_list[i] = one_diff
        print("one_diff_list : {}".format(one_diff_list))

        target_index = total_words.index(target)
        visited = [False] * total_words_size
        stack = []
        stack.extend(one_diff_list[0])
        visited[0] = True
        answer = browse(x, target_index, visited, one_diff_list, stack, count, answer)

        dq.extend(one_diff_list[0])
        print("init_dq : {}".format(dq))
        target_index = total_words.index(target)
        while dq:
            x = dq.popleft()
            temp = 1
            if x == target_index:
                answer += 1
                continue

            for i in one_diff_list[x]:
                dq.append(i)

    return answer
