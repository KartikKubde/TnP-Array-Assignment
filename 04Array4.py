# Find the Second Largest Element

class Solution:
    def getSecondLargest(self, arr):
        large = -1
        second_large = -1
        n = len(arr)

        for i in range(n):
            if( arr[i] > large):
                second_large = large
                large = arr[i]
            elif( arr[i] < large and arr[i] > second_large):
                second_large = arr[i]
        
        return second_large