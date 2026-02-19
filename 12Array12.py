# 12. Find the Missing Number: Find the missing number in an array of size n containing numbers from 1 to n.

# Leetcode 268. Missing Number

class Solution:
    def missingNumber(self, nums) -> int:
        n = len(nums)

        total_sum = n*(n+1)//2

        sum = 0

        for i in range(len(nums)):
            sum += nums[i]

        ans = total_sum - sum

        return ans