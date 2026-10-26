#Given an array and an integer k, rotate the array to the right by k positions.

arr = [1, 2, 3, 4, 5, 6, 7]
k = 3

arr.reverse()
print(arr)
arr[0:k] = arr[0:k][::-1]
print(arr)
arr[k::] = arr[k::][::-1]
print(arr)