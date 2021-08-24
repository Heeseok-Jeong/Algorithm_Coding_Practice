def solution(N, number):
    answer = 0
    cases = [0, [N]]
    if N == number:
        return 1
    
    for count in range(2, 9):
        temp_cases = [int(str(N)*count)]
        for i in range(1, count//2 + 1):
            for x in cases[i]:
                for y in cases[count-i]:
                    temp_cases.append(x+y)
                    temp_cases.append(x-y)
                    temp_cases.append(y-x)
                    temp_cases.append(x*y)
                    if y != 0:
                        temp_cases.append(x//y)
                    if x != 0:
                        temp_cases.append(y//x)
        if number in temp_cases:
            return count
        cases.append(temp_cases)
        
    return -1

N, number = map(int, input().split())
print(solution(N, number))