# 28. Sort an Array of 0s, 1s, and 2s: Sort an array consisting of only 0s, 1s, and 2s.

# Leetcode 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1

        while(mid<=high):
            if(nums[mid] == 0):
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif(nums[mid] == 1):
                mid+=1

            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
