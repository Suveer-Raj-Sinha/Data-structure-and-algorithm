#Given a sorted array, remove duplicates in-place without using set() or creating another array.

arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
n = len(arr)
j = 0

for i in range(1, n):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]

for i in range(n - (j+1)):
    arr.pop()        

print(arr)