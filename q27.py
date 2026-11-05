#Find the Equilibrium Index - An equilibrium index is an index where the sum of elements on the left equals the sum of elements on the right.

arr = [1, 3, 5, 2, 2]
n = len(arr)

for i in range(n):
    sum1 = 0
    sum2 = 0
    for j in range(i):
        sum1 += arr[j]
    for k in range(i+1, n):
        sum2 += arr[k]

    if sum1 == sum2:
        print(f"Element : {arr[i]}")
        print(f"Index : {i}")