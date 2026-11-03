# Given an array, find all pairs whose sum equals the target.

arr = [1, 5, 7, -1, 5]
target = 6

for i in range(len(arr)):
    nums = []
    for j in range(i, len(arr)):
        if arr[i] + arr[j] == target:
            nums.append(arr[i])
            nums.append(arr[j])
            print(nums)
            break