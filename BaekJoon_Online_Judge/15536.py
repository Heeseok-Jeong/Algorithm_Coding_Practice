from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
p = list(permutations(arr, M))
p = sorted(list(set(p)))
for nums in p:
    for x in nums:
        print(x, end=' ')
    print()