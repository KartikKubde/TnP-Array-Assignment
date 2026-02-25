# 15. Find Union of Two Arrays

class Solution:
    def findUnion(self, a, b):
        
        i = 0 
        j = 0 
        
        c = []
        
        m = len(a)
        n = len(b)
        
        while(i<m and j<n):
            if(a[i] == b[j]):
                if not c or c[-1] != a[i]:
                    c.append(a[i])
                i += 1
                j += 1
            elif(a[i] < b[j]):
                if not c or c[-1] != a[i]:
                    c.append(a[i])
                i+=1
            else:
                if not c or c[-1] != b[j]:
                    c.append(b[j])
                j+=1
                
        while(i<m):
            if not c or c[-1] != a[i]:
                c.append(a[i])
            i+=1
            
        while(j<n):
            if not c or c[-1] != b[j]:
                c.append(b[j])
            j+=1
            
        return c