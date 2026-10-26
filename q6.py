#Given an array of integers, determine whether it is sorted in non-decreasing order.

arr = [1, 2, 2, 4, 7]
isdescending = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i+1]:
        isdescending = False
        break
    
print(isdescending)