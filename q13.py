#Given an array and a target number, count how many times the target appears.

arr = [1, 2, 3, 2, 4, 2, 5, 2]
target = 2
count = 0

for i in arr:
    if i == target:
        count += 1

print(count)