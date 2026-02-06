class Solution:  
    def findUnion(self, a, b):
        # code here
        # union = []
        # seen = set()
        
        s1 = set(a)
        s2 = set(b)
        
        un = s1 | s2
        
        return [i for i in un]

        # for x in a + b:
        #     if x not in seen:
        #         seen.add(x)
        #         union.append(x)
    
        # return union