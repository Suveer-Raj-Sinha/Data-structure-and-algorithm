# Given two arrays, check whether they contain exactly the same elements in the same order.

arr1 = [1, 2, 3, 4]
arr2 = [1, 2, 3, 4]

isequal = len(arr1) == len(arr2)

for i in range(len(arr1)):
    if arr1[i] != arr2[i]:
        isequal = False
        break

print("Equal" if isequal else "Not equal")