# Given two arrays, find the elements that are present in both arrays. Return each common element only once.

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 4, 5, 6]
common = []

for i in arr1:
    for j in arr2:
        if i == j:
            if i not in common:
                common.append(i)

print(common)