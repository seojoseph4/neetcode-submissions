class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        n2= len(matrix[0])
        firstrow = False
        firstcol = False
        for i in range(n):
            for j in range(n2):
                if matrix[i][j] == 0:
                    if i == 0:
                        firstrow = True
                    if j == 0:
                        firstcol = True
                    matrix[0][j] =0
                    matrix[i][0] = 0
                    
        print(matrix)
        #Rows
        for i in range(1,n):
            if matrix[i][0] == 0:
                for j in range(n2):
                    matrix[i][j] = 0
        
        #Cols
        for i in range(1,n2):
            if matrix[0][i] == 0:
                for j in range(n):
                    matrix[j][i] = 0
                

        if firstrow:
            for i in range(n2):
                matrix[0][i] = 0
        if firstcol:
            for i in range(n):
                matrix[i][0] = 0


        
        