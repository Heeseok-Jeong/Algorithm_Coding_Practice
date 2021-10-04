def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    
    for i, price in enumerate(prices):
        while stack and (prices[stack[-1]] > price):
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    
    while stack:
        j = stack.pop()
        answer[j] = i - j

    return answer
    