# Given an unsorted array, find the length of the longest sequence of consecutive numbers.

arr = [100, 4, 200, 1, 3, 2]
max_length = 0

for i in arr:
    count = 1
    num = i

    while num + 1 in arr:
        count += 1
        num += 1

    if count > max_length:
        max_length = count

print(max_length)