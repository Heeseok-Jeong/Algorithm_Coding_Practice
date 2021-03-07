N = int(input())
for _ in range(N):
    H, W, N = map(int, input().split())
    result = str((N-1)%H + 1)
    if (N-1)//H + 1 < 10:
        result += "0"
    result += str((N-1)//H + 1)
    print(result)
