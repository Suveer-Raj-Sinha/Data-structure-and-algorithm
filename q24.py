# Given an array containing numbers from 1 to n, with one number missing, find the missing number.

arr = [1, 2, 4, 5, 6]
n = len(arr) + 1

for i in range(1, n+1):
    if i not in arr:
        print(i)