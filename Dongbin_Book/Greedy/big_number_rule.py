n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse = True)

answer = 0

for i in range(m):
    if i % k == 0 and i != 0:
        answer += arr[1]
    else:
        answer += arr[0]

print(answer)
