nums = input()

result = int(nums[0])
for i in range(1, len(nums)):
    if int(nums[i]) <= 1 or result <= 1:
        result += int(nums[i])
    else:
        result *= int(nums[i])

print(result)
