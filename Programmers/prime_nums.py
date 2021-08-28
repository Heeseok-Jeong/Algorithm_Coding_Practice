from itertools import permutations
def solution(numbers):
    answer = 0    
    LIMIT = int(1e7)
    prime_nums = [True for _ in range(LIMIT+1)]
    prime_nums[1] = False
    prime_nums[0] = False
    for i in range(2, LIMIT):
        if prime_nums[i]:
            for j in range(2*i, LIMIT, i):
                prime_nums[j] = False
    
    permus = set()
    for l in range(1, len(numbers)+1):
        permu = list(permutations(numbers, l))
        for p in permu:
            permus.add(int(''.join(p)))
            
    for p in permus:
        if prime_nums[p]:
            answer += 1
    return answer