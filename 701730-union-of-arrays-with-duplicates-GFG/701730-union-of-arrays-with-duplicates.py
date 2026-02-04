class Solution:  
    def findUnion(self, a, b):
        # code here
        union = []
        seen = set()

        for x in a + b:
            if x not in seen:
                seen.add(x)
                union.append(x)
    
        return union