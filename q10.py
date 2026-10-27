#Given an array, reverse its elements in-place.

arr = [10, 20, 30, 40, 50]
n = len(arr)
j = n - 1
i = 0

while i < n-1:
    if i >= j:
        break
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1

print(arr)