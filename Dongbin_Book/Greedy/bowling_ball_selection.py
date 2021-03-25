N, M = map(int, input().split())

arr = list(map(int, input().split()))
balls = {}
for x in arr:
    try:
        balls[x] += 1
    except:
        balls[x] = 1

# for item in balls.items():
#     print(item)

count = N
result = 0
for v in balls.values():
    count -= v
    result += v*count

print(result)
