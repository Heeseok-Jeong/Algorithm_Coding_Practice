import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

name_set = set()

for _ in range(N):
    name = input().rstrip()
    name_set.add(name)

result = []
for _ in range(M):
    name = input().rstrip()
    if name in name_set:
        result.append(name)

result.sort()
result_len = len(result)
print(result_len)
if result_len != 0:
    for name in result:
        print(name)
