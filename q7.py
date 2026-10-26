#An array contains n - 1 distinct numbers from the range 1 to n. Find the one missing number.

arr = [1, 2, 3, 4, 6]
n = len(arr) + 1

# for i in range(n-1):
#     if i+1 != arr[i]:
#         print(i+1)
#         break

total = sum(arr)
missing_num = n*(n+1)//2 - total

print(f"Missing number: {missing_num}")