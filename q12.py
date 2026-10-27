#Given an array of integers, count how many numbers are even and how many are odd.

arr = [2, 5, 8, 11, 14, 17, 20]
even = 0
odd = 0

for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"Even: {even}")
print(f"Odd: {odd}")