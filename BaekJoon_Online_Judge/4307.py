import sys 

input = sys.stdin.readline

def get_fastest_time(ants, L, N):
    fastest_time = 0

    for x in ants:
        fastest_time = max(fastest_time, x) if x < L-x else max(fastest_time, L-x)

    return fastest_time

def get_slowest_time(ants, L, N):
    slowest_time = 0

    for x in ants:
        slowest_time = max(slowest_time, L-x) if x < L-x else max(slowest_time, x)

    for i in range(1, N):
        mid = (ants[i]+ants[i-1])/2 
        time = int(max(mid, L-mid) + (mid - ants[i-1]))
        slowest_time = max(slowest_time, time)

    return slowest_time


T = int(input().rstrip())
results = []
for _ in range(T):
    L, N = map(int, input().rstrip().split())
    ants = []
    for _ in range(N):
        ants.append(int(input().rstrip()))
    ants.sort()
    results.append((get_fastest_time(ants, L, N), get_slowest_time(ants, L, N)))

for fastest_time, slowest_time in results:
    print(f"{fastest_time} {slowest_time}")
