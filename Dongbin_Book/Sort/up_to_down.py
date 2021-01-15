n = int(input())
arr = [int(input()) for _ in range(n)]
arr.sort(reverse = True)

for x in arr:
    print(x, end = ' ')
