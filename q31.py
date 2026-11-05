# Given an array, rotate it to the left by k positions.
# Manual without using reverse

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
new_arr = []

for i in range(k, len(arr)):
    new_arr.append(arr[i])
for i in range(k):
    new_arr.append(arr[i])
arr = new_arr
print(arr)