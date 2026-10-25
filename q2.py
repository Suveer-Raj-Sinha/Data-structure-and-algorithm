#Program to move all zeros of an array to the end of the array

array=[0, 1, 0, 3, 12, 0]
j = 0

#for moving to back 
for i in range(len(array)):
    if(array[i] != 0):
        array[j], array[i] = array[i], array[j]
        j = j + 1  

print(array)
