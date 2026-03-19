class Solution:
    def lastRemaining(self, n: int) -> int:
        l, r = 1, n
        gp = 1
        x = 0
        size = n
        while l < r:
            if x%2 == 0: 
                l += gp
                if size%2 == 1:
                    r -= gp
            else:
                r -= gp
                if size%2 == 1: 
                    l += gp
            gp *= 2
            x += 1
            size //= 2

        return l