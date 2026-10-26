#Given an array of integers and a target value, find the indices of two different elements whose sum equals the target.

arr = [2, 7, 11, 15]
target = 9
output = []

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i] + arr[j] == target:
            output.append(i)
            output.append(j)
    break

print(output)