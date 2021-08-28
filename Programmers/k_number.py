def solution(array, commands):
    answer = []
    for begin, end, n in commands:
        temp = sorted(array[begin-1:end])
        answer.append(temp[n-1])
    return answer