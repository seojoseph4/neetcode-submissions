class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols=len(matrix[0])
        l = 0
        r = cols*rows -1

        while l <= r:
            m = (l+r) // 2
            ro = m //cols
            co = m % cols
            # print(ro, co)
            if matrix[ro][co] == target:
                return True
            if matrix[ro][co] < target:
                l = m+1
            else:
                r = m-1
        return False



        