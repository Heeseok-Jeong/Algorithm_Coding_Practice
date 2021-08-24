def count_target(d, n_size, numbers, n_sum, target, answer):
    if d == n_size:
        if n_sum == target:
            answer += 1
        return answer

    answer = count_target(d+1, n_size, numbers, n_sum+numbers[d], target, answer)
    answer = count_target(d+1, n_size, numbers, n_sum-numbers[d], target, answer)
    return answer

def solution(numbers, target):
    answer = 0
    d = 0
    n_sum = 0
    n_size = len(numbers)
    answer = count_target(d, n_size, numbers, n_sum, target, answer)
    return answer

numbers = [1,1,1,1,1]
target = 3
answer = solution(numbers, target)
print(answer)
