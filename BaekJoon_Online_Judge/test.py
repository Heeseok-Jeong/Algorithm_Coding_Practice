def binary_search(array, x):
    left = 0
    right = len(array)
    mid = 0
    step = 0

    while(left <= right):
        print(f"step : {step}, subarray : {array[left:right-1]}")
        step += 1
        mid = (left+right) // 2
        if x == array[mid]:
            return mid
        
        if x < array[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print(f"The answer is {binary_search([i for i in range(35)], 2)}")
