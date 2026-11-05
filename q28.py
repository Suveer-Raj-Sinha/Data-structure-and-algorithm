# Given an array of positive integers, find the continuous subarray whose sum equals the target.

arr = [1, 2, 3, 7, 5]
target = 12

for i in range(len(arr)):
    sum = 0
    con_arr = []
    for j in range(i, len(arr)):
        sum += arr[j]
        con_arr.append(arr[j])
        if sum == target:
            print(con_arr)
            break
        elif sum > target:
            break
