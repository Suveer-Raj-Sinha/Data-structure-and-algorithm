#Given an array of integers, find the second-smallest distinct element without sorting the array.

arr = [7, 2, 9, 2, 4, 1]
smallest = arr[0]
second_smallest = arr[0]

for i in arr:
    if i < smallest:
        second_smallest = smallest
        smallest = i
    if i > smallest and i < second_smallest:
        second_smallest = i

print(f"Second smallest: {second_smallest}")
# print(smallest)