N, L = map(int, input().split())
D = [0 for _ in range(N+1)]
R = [0 for _ in range(N+1)]
G = [0 for _ in range(N+1)]
for i in range(1, N+1):
    D[i], R[i], G[i] = map(int, input().split())
total_time = 0

for i in range(1, N+1):
    total_time += D[i] - D[i-1]
    cycle = R[i] + G[i]
    mod = total_time % cycle
    if mod < R[i]:
        total_time += R[i] - mod 
total_time += L - D[N]

print(total_time)
