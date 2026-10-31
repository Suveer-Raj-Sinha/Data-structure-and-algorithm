#Given an array and a target number, find out how many times the target appears in the array.

arr = [4, 2, 4, 3, 2, 4, 1]
target = 4
count = 0

for i in arr:
    if i == target:
        count += 1

print(count)