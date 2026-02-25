# 23. Maximum Sum Subarray (Kadane's Algorithm)

# Leetcode 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_ending = nums[0]
        ans = nums[0]

        for i in range(1,len(nums)):
            v1 = best_ending + a[i]
            v2 = a[i]

            best_ending = max(v1,v2)
            ans = max(ans,best_ending)

        return ans