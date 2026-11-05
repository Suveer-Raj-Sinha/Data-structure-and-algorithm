# Given an array of integers, find the maximum possible sum of a continuous subarray.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
max = arr[0]

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        if sum > max:
            max = sum

print(max)