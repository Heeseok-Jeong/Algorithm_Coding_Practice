from itertools import combinations

N, M = map(int, input().split())
houses, chickens = [], []

for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 1:
            houses.append((i, j))
        elif line[j] == 2:
            chickens.append((i, j))    

combis = list(combinations(chickens, M))
result = 1e9
for combi in list(combis):
    combi_sum = 0
    for h_i, h_j in houses:
        h2c_dist = 1e9
        for c_i, c_j in combi:
            h2c_dist = min(h2c_dist, abs(h_i-c_i) + abs(h_j-c_j))
        combi_sum += h2c_dist
    result = min(result, combi_sum)

print(result)
