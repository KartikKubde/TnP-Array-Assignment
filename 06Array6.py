# 6. Check if Array is Sorted

class Solution:
    def isSorted(self, arr) -> bool:
        n = len(arr)
        
        for i in range(n-1):
            if arr[i] > arr[i+1] :
                return False
                
        return True
    
# T.C. = O(n)
# S.C. = O(1)