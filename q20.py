# Given two arrays, find all elements that are present in the first array but not in the second array.

arr1 = [1, 2, 3, 4, 5, 6]
arr2 = [2, 4, 6]
not_common = []

for i in arr1:
    if i not in arr2:
        not_common.append(i)

print(not_common) 