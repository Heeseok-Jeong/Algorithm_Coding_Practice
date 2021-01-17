x = int(input())

memo = [0 for _ in range(x+1)]
for i in range(2,x+1):
    nums = []
    if i % 5 == 0:
        nums.append(memo[i//5] + 1)
    if i % 3 == 0:
        nums.append(memo[i//3] + 1)
    if i % 2 == 0:
        nums.append(memo[i//2] + 1)
    nums.append(memo[i-1] + 1)
    memo[i] = min(nums)

print(memo[x])
