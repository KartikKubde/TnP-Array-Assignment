#2. Find the Maximum & Minimum Element

arr = [6,4,7,1,3]

# For max
max = float('-inf')

for i in range(len(arr)):
    if(arr[i] > max):
        max = arr[i]

print(max)

# For min
min = float('inf')

for i in range(len(arr)):
    if(arr[i] < min):
        min = arr[i]

print(min)