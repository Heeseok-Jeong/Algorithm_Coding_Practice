def solution(priorities, location):
    answer = 0
    q = [(priorities[i], i) for i in range(len(priorities))]
    
    while q:
        max_index = list(zip(*q))[0].index(max(list(zip(*q))[0]))
        q = q[max_index:] + q[:max_index]
        n = q.pop(0)
        answer += 1
        if n[1] == location:
            break
    return answer
    