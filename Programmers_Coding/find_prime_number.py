from itertools import permutations

def make_prime(max_num):
    prime_set = set()
    range_set = [True] * (max_num+1)

    for prime in range(2, max_num+1):
        if range_set[prime]:
            for num in range(prime*2, max_num+1, prime):
                range_set[num] = False
    for num in range(2, max_num+1):
        if range_set[num]:
            prime_set.add(num)
    return prime_set

def solution(numbers):
    answer = 0
    numbers_list = list(numbers)
    permu_set = set()
    for i in range(len(numbers_list)):
        permu_set |= set(map(int, map(''.join, permutations(numbers_list, i+1))))

    prime_set = set()
    max_prime_set = set()
    max_num = max(permu_set)
    max_prime_set = make_prime(max_num)
    for num in permu_set:
        if num in max_prime_set:
            answer += 1
    return answer

numbers = input()
answer = solution(numbers)
print(answer)
