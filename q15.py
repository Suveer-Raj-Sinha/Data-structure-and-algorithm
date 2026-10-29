#Given an array of integers, check whether it reads the same forward and backward.

arr = [1, 2, 3, 2, 1]
n = len(arr)
palindrome = True
j = n-1

for i in arr:
    if i != arr[j]:
        palindrome = False
        break
    j -= 1

print("Palindrome" if palindrome else "Not Palindrome")  