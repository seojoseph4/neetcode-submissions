class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows * cols

        l, r = 0, total-1

        while l<=r:
            m = (l+r) //2
            co = m % cols
            ro = m // cols
            if matrix[ro][co] == target:
                return True
            if matrix[ro][co] < target:
                l = m+1
            else:
                r = m-1

        return False 

        