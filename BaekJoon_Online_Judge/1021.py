from collections import deque

def move_r(list_):
    list_.appendleft(len(list_)-1)
    list_.pop()
    return list_

def move_l(list_):
    list_.append(list_[0])
    list_.popleft()
    return list_

def solve(deq_):
    result = 0
    for x in info:
        idx = deq_.index(x)
        left = len(deq_)-idx-1
        right = len(deq_)-left
        if left < right:
            for i in range(left):
                deq_ = move_l(deq_)
                result += 1
        else:
            for i in range(right):
                deq_ = move_l(deq_)
                result += 1

    return result

n, m = map(int, input().split())
info = list((map(int, input().split())))
deq_ = deque(i for i in range(1, n+1))
result = solve(deq_)
print(result)
