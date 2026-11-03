# Given an array, find the element that appears more than n/2 times.

arr = [2, 2, 1, 2, 3, 2, 2]
n = len(arr) / 2


for i in arr:
    count = 0
    for j in arr:
        if i == j:
            count += 1

    if count > n:
        print(i)
        break

            