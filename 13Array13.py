# 13. Find Duplicates in an Array

nums = [4,3,2,7,8,2,3,1]
dict = {}
n = len(nums)
ans = []

for i in range(n):
    dict[nums[i]] = dict.get(nums[i],0) + 1

    if(dict[nums[i]] == 2):
        ans.append(nums[i])

print(ans)