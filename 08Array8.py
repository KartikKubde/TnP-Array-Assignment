# 8. Find Pair with Given Sum: Find a pair of elements that adds up to a target sum.

arr = [2,4,5,7,10]
target = 11

n = len(arr)
i = 0 
j = n - 1

while(i<j):
    sum = arr[i] + arr[j]

    if(sum < target):
        i += 1
    elif(sum > target):
        j -= 1
    else:
        print(i," ",j)
        break