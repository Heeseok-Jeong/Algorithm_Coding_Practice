n = int(input())
scores = [list(input().split()) for _ in range(n)]
scores.sort(key = lambda x : int(x[1]))

for name, _ in scores:
    print(name, end = ' ')
