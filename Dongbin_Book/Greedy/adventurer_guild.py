N = int(input())

arr = list(map(int, input().split()))
arr.sort()

result = 0
count = 0
for x in arr:
    count += 1
    if count >= x:
        result += 1
        count = 0

print(result)
