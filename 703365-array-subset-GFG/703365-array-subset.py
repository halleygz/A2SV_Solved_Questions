#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        frq = {}
        for x in a:
            if x in frq:
                frq[x] += 1
            else:
                frq[x] = 1
            
            
        for x in b:
            if x not in frq or frq[x] == 0:
                return False
            frq[x] -= 1
            
        return True
    
    
    
