import sys

input = sys.stdin.readline

n = int(input().rstrip())
poles = list(map(int, input().rstrip().split()))
poles = [1e9 + 1] + poles
connected = [0 for _ in range(n+1)]

for i in range(2, n+1):
    if poles[i-1] < poles[i]:
        j = connected[i-1]
        while True:
            if poles[j] < poles[i]:
                j = connected[j]
            else:
                connected[i] = j
                break
    else:
        connected[i] = i-1

for x in connected[1:]:
    print(x, end=' ')
