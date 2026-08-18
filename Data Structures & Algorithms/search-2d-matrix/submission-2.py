class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) -1
        left = 0
        right = len(matrix[0]) -1
        while bottom >= top:
            m = (top+bottom) //2 
            if target < matrix[m][left]:
                bottom = m-1
            elif target > matrix[m][right]:
                top = m+1
            else:
                break
        

        while left <= right:
            m2 =(left+right)//2
            if matrix[m][m2] == target:
                return True
            elif target < matrix[m][m2]:
                right = m2-1
            else:
                left = m2+1
        
        return False


        