#Find the largest element without using a function

arr = [14, 7, 29, 3, 18, 22]
largest = 0

for i in arr:
    if i > largest:
        largest = i

print(largest)