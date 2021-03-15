import sys

input = sys.stdin.readline

arr = [0, 1, 2, 4]
for i in range(4, 11):
    arr.append(arr[i-1] + arr[i-2] + arr[i-3])

T = int(input())
for _ in range(T):
    x = int(input())
    print(arr[x])
