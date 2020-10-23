import heapq
import sys

input = sys.stdin.readline
n = int(input())
arr = []
result = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if arr:
            result.append(heapq.heappop(arr))
        else:
            result.append(0)
    else:
        heapq.heappush(arr, x)

for x in result:
    print(x)
