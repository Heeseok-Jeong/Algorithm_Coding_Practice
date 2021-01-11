n, _ = map(int, input().split())
answer = 0
for _ in range(n):
    x = min(list(map(int, input().split())))
    if answer < x:
        answer = x

print(answer)
