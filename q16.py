# An element is called a leader if it is greater than or equal to every element to its right. The last element is always a leader.

arr = [16, 17, 4, 3, 5, 2]
leader = []
n = len(arr)
j = n-2

for i in reversed(arr):
    if i > arr[j]:
        leader.append(arr[j])
        j -= 1
    else: 
        breakgit

print(leader)