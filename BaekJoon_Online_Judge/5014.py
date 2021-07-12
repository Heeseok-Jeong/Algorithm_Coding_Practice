from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [False for _ in range(F+2)]
counts = [0 for _ in range(F+2)]
floors = deque()
floors.append(S)

buttons = []
if U != 0:
    buttons.append(U)
if D != 0:
    buttons.append(-D)

while floors:
    floor = floors.popleft()
    if visited[floor]:
        continue
    if floor == G:
        break
    visited[floor] = True
    for value in buttons:
        new_floor = floor + value
        if 1<=new_floor<=F and not visited[new_floor]:
            counts[new_floor] = counts[floor] + 1
            floors.append(new_floor)

if S == G:
    answer = 0
elif counts[G] > 0:
    answer = counts[G]
else:
    answer = "use the stairs"
print(answer)
