class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        
        row_track = [0 for _ in range(0, row)]
        col_track = [0 for _ in range(0, col)]

        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1
        
        for i in range(0, row):
            for j in range(0, col):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0
        
        return matrix

