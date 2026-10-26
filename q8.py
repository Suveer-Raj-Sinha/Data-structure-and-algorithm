#Given an array of integers, move all negative numbers to the left and all non-negative numbers to the right.

arr = [3, -1, 4, -2, 0, -5, 8]
n = len(arr)
j = n-1
i = 0

while i < j:
    if arr[i] < 0:
        i += 1
    elif arr[j] >= 0:
        j -= 1
    else:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j += 1

print(arr)