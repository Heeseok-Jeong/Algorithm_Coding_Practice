import sys
import heapq

input = sys.stdin.readline

n = int(input())
ref = {}
abs_arr = []
result = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if abs_arr:
            key = heapq.heappop(abs_arr)
            result.append(heapq.heappop(ref[key]))
        else:
            result.append(0)
    else:
        key = abs(x)
        heapq.heappush(abs_arr, key)
        if not ref.get(key, 0):
            ref[key] = [x]
        else:
            heapq.heappush(ref[key], x)

for x in result:
    print(x)
