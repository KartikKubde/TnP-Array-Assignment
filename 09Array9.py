# 9. Remove Duplicates from Array

arr = [1,1,2,2,2,3,3,4]

n = len(arr)
i = 1 
j = 0

while(i<n):
    if(arr[i] != arr[j]):
        arr[j+1] = arr[i]
        j += 1
        i += 1
    else:
        i += 1

print(arr)