# 5. Count Frequency of Elements

class Solution:
    def countFreq(self, arr):
        dict = {}
        n = len(arr)
        
        for i in range(n):
            if arr[i] in dict:
                dict[arr[i]] += 1
            else:
                dict[arr[i]] = 1
                
        result = []
        
        for key in dict:
            result.append([key,dict[key]])
                
        return result
    
# T.C. = O(n)
# S.C. = O(n)