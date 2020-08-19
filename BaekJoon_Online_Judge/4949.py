import sys

def read_sys():
    return sys.stdin.readline()

def solve():
    return

flag = True
while flag:
    stack = []
    result = "yes"
    str_ = read_sys()
    if str_[0] == '.' and len(list(str_)) == 2:
        flag = False
    else:
        for chr_ in str_:
            if chr_ == '(' or chr_ == '[' or chr_ == ')' or chr_ == ']':
                stack.append(chr_)
            if stack:
                if stack[0] == ']' or stack[0] == ')':
                    result = 'no'
                    break
                if chr_ == ')' and stack[len(stack)-2] == '(':
                    stack.pop()
                    stack.pop()
                if chr_ == ']' and stack[len(stack)-2] == '[':
                    stack.pop()
                    stack.pop()
        if len(stack) != 0:
            result = 'no'
    if flag == True:
        print(result)
