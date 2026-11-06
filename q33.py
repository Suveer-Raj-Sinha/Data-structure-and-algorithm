# An array contains numbers from 1 to n. One number is missing and another number is repeated. Find both.

arr = [1, 2, 2, 4, 5]
n = len(arr)

for i in range(n):
    for j in range(i+1, n):
        if arr[i] == arr[j]:
            print(f"Duplicate : {arr[i]}")
    if i+1 not in arr:
        print(f"Misiing : {i+1}")