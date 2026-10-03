class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix)-1

        while left < right:
            for i in range(right-left):
                top, bottom = left, right

                topLeft = matrix[top][left+i]

                #bottom left --> top left
                matrix[top][left+i] = matrix[bottom-i][left]
                #bottom right --> bottom left
                matrix[bottom-i][left] = matrix[bottom][right-i]
                #topright --> bottom right
                matrix[bottom][right-i] = matrix[top+i][right]
                #topleft --> top right
                matrix[top+i][right] = topLeft

            right-=1
            left+=1

