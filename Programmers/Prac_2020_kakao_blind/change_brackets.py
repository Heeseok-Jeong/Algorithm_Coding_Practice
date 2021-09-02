def check_right_str(p):
    count = 0
    for a in p:
        if a == "(":
            count += 1
        else:
            count -= 1
        
        if count < 0:
            return False
    return True

def split_u_v(p):    
    u = []
    v = []
    count = 0
    if p[0] == "(":
        count += 1
    else:
        count -= 1
        
    for i in range(1, len(p)):
        if p[i] == "(":
            count += 1
        else:
            count -= 1
        
        if count == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
    return u, v

def reverse_brackets(u):
    reversed_u = ''
    for a in u:
        temp = ')' if a == '(' else '('
        reversed_u += temp
    return reversed_u
        
def solution(p):
    answer = ''
    # 1    
    if not p or check_right_str(p):
        answer = p
        return answer
    
    # 2
    u, v = split_u_v(p)
    
    # 3
    if check_right_str(u):
        answer =  u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        answer += reverse_brackets(u[1:-1])
    
    return answer
    