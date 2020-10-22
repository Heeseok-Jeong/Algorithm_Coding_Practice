def solution(number, k):
    answer = ''
    numbers = list(map(int, number))
    collected = []
    pivot = 0
    count = 0

    for i, num in enumerate(numbers):
        if pivot < num:
            while collected and count != k:
                x = collected.pop()
                if num <= x:
                    collected.append(x)
                    break
                count += 1

        collected.append(num)
        pivot = num

    for _ in range(k-count):
        collected.pop()

    answer = ''.join(map(str, collected))

    return answer

number = "1231234"
k = 3
answer = solution(number, k)
print(answer)
