#Given an array of integers, find the largest number in the array without using built-in functions.

arr = [15, 3, 9, 22, 8]
max_val = arr[0]

for i in arr:
    if i > max_val:
        max_val = i

print(max_val)