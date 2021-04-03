# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s)
    STR, CNT = 0, 1
    
    for cut in range(1, len(s)//2+1):
        splited = [s[i:i+cut] for i in range(0, len(s), cut)]
        compressed = ""
        stack = [[splited[0], 1]]
        for x in splited[1:]:
            if stack[-1][STR] == x:
                stack[-1][CNT] += 1
            else:
                if stack[-1][CNT] > 1:
                    compressed += str(stack[-1][CNT])
                compressed += stack[-1][STR]
                stack.append([x, 1])
        if stack[-1][CNT] > 1:
            compressed += str(stack[-1][CNT])
        compressed += stack[-1][STR]
            
        answer = min(answer, len(compressed))        
            
    return answer
    