from collections import deque

def solve():
    # queue = deque(i for i in range(1, n+1))
    queue = [i for i in range(0, n+1)]
    temp = []
    index = 0
    check = 0
    times = 0
    while times != n-1:
        for _ in range(k):
            check += 1
            if index == len(queue)-1:
                 index = 1
            else:
                index += 1
        if check == k:
            x = queue[index]
            temp.append(str(x))
            del queue[index]
            check = 0
            index -= 1
            times += 1

    temp.append(str(queue[1]))
    return temp


n, k = map(int, input().split())
temp = solve()
result = '<'
result += ', '.join(temp)
result += '>'
print(result)
