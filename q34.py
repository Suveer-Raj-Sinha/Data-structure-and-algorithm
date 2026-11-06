# Given an array of integers, find the first element that appears exactly once.

arr = [4, 5, 1, 2, 1, 4, 5]

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count == 1:
        print(arr[i])
        break