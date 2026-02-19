#10. Merge Two Sorted Arrays

arr1 = [1,4,5,7,8]
arr2 = [2,3,5,9,10,11]

res = []

i = 0
j = 0
k = 0 

m = len(arr1)
n = len(arr2)

while(i<m and j<n):
    if( arr1[i] < arr2[j]):
        res.append(arr1[i])
        k += 1
        i += 1
    elif(arr1[i] > arr2[j]):
        res.append(arr2[j])
        k += 1
        j += 1
    else:
        res.append(arr1[i])
        k += 1
        i += 1

while(i<m):
    res.append(arr1[i])
    k += 1
    i += 1

while(j<n):
    res.append(arr2[j])
    k += 1
    j += 1

print(res)