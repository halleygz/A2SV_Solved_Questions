class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        keys = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j >= len(keys):
                    keys.append([])
                keys[i+j].append(mat[i][j])

        res = []
        for i in range(len(keys)):
            if i % 2 == 0:
                res.extend(reversed(keys[i]))
            else:
                res.extend(keys[i])

        return res