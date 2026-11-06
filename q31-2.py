# Given an array, rotate it to the left by k positions.
# Using reverse

arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
n = len(arr)
k %= n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(gcd(n, k)):
    temp = arr[i]
    j = i

    while True:
        d = (j + k) % n

        if d == i:
            break

        arr[j] = arr[d]
        j = d

    arr[j] = temp

print(arr)