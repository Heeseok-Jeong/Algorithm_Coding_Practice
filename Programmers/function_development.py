def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        i = 0
        while progresses[i] >= 100:
            i += 1
            if i == len(progresses):
                break

        if i != 0:
            answer.append(i)
            progresses = progresses[i:]
            speeds = speeds[i:]
        
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))