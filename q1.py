# Find second largest element in array

largest = 0
second_largest = 0
array = [5, 8, 3, 8, 6, 2]

for i in array:
    if(i > largest):
        second_largest = largest
        largest = i
    if(i < largest and i > second_largest ):
        second_largest = i

print(largest)
print(second_largest)
