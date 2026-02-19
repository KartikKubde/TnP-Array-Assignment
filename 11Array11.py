# 11. Remove given Element from Array
# Leetcode 27 Remove Element

class Solution:
    def removeElement(self, nums, val: int) -> int:
        n = len(nums)
        i = 0
        j = 0

        while(i<n):
            if(nums[i] == val):
                i+=1
            else:
                nums[j] = nums[i]
                j+=1
                i+=1

        return j
    
# T.C. = O(n)
# S.C. = O(1)