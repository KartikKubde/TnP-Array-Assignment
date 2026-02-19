#1. Reverse an Array

arr = [2,4,3,5,7]
arr2 = [1,3,4,6]

i = 0
j = len(arr) - 1

while(i<=j):
    arr[i] , arr[j] = arr[j] , arr[i]
    i = i + 1
    j = j - 1
print(arr)

