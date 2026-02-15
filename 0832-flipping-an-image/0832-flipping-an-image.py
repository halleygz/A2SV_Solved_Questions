class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in image:
            temp = []
            for px in list(reversed(i)):
                if px == 1:
                    temp.append(0)
                else:
                    temp.append(1)
            res.append(temp)
            temp = []
        return res
        