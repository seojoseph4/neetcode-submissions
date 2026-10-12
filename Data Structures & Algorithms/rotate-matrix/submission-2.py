class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left = 0
        right = len(matrix)-1
        while left < right:

            top = left
            bottom = right
            for i in range(right-left):
                topleft = matrix[top][left+i]
                topright = matrix[top+i][right]
                bottomleft = matrix[bottom-i][left]
                bottomright = matrix[bottom][right-i]

                matrix[top][left+i] = bottomleft
                matrix[top+i][right] = topleft
                matrix[bottom][right-i] = topright
                matrix[bottom-i][left] = bottomright
            left+=1
            right-=1
        