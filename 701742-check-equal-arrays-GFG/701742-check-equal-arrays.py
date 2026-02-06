class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        sortedA = sorted(a)
        sortedB = sorted(b)
        
        for i in range(len(sortedA)):
            if sortedA[i] != sortedB[i]:
                return False
        return True