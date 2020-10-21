from collections import deque

dq = deque()
dq.append(5)
dq.appendleft(3)
print(dq)
dq.appendleft(1)
dq.pop()
dq.popleft()
print(dq)
