class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        rowzero = False
        colzero = False
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        rowzero = True
                    else:
                        matrix[r][0] = 0
                    if c == 0:
                        colzero = True
                    else:
                        matrix[0][c] = 0
        for r in range(1,rows):
            if matrix[r][0] == 0:
                for c in range(1,cols):
                    matrix[r][c] = 0
            
        
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0
        if rowzero:
            for c in range(0,cols):
                matrix[0][c] = 0
        if colzero:
            for r in range(0, rows):
                matrix[r][0] = 0

