#Given an array of integers, find the first element that appears more than once, scanning from left to right.

arr = [5, 3, 4, 3, 5, 6]
arr2 = []

for i in arr:
    if i in arr2:
        print(i)
        break
    arr2.append(i)