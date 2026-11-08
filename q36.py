# Given an array, remove every occurrence of a target element in-place.

arr = [3, 2, 2, 3, 4, 2, 5]
target = 2

count = arr.count(target)
for i in range(count+1):
    if target in arr:
        arr.remove(target)

print(arr)