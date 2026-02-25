class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []

        for row in image:
            flipped = []
            for px in row[::-1]:
                if px == 0:
                    flipped.append(1)
                else:
                    flipped.append(0)
                
            res.append(flipped)

        return res
