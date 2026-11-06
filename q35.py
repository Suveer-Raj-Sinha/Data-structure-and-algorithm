# Given an array, find the element with the second-highest frequency.

arr = [1, 1, 1, 2, 2, 3, 3, 3, 3]
max = arr[0]
second_max = arr[0]
max_freq = 0
second_max_freq = 0

for i in range(len(arr)):
    count = 0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count += 1

    if count > max_freq:
        second_max = max
        second_max_freq = max_freq

        max_freq = count
        max = arr[i]

    elif count > second_max_freq and arr[i] != max:
        second_max_freq = count
        second_max = arr[i]

print(second_max)