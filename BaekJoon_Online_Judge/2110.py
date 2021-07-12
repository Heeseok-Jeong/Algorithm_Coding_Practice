import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()

l = 1
r = houses[-1] - houses[0]
while l <= r:
    mid = (l+r) // 2
    count = 1
    pivot = houses[0]
    for i in range(1, N):
        if houses[i]-pivot >= mid:
            pivot = houses[i]
            count += 1
            if count == C:
                break

    if count == C:
        l = mid+1
        answer = mid
    elif count < C:
        r = mid-1

print(answer)
