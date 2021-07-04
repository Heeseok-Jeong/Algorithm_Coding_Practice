from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(1, N+1):
    parts = list(combinations(arr, i))
    for part in parts:
        if sum(part) == S:
            answer += 1
        
print(answer)
    