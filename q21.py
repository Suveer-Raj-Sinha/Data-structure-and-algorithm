# Given an array, find the maximum difference arr[j] - arr[i] such that j > i.

arr = [2, 3, 10, 6, 4, 8, 1]
min = arr[0] 
max_diff = arr[1] - arr[0]

for i in arr:
    diff = i - min
    if diff > max_diff:
        max_diff = diff
    if i < min:
        min = i

print(max_diff)