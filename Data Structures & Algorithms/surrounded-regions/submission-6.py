class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        def helper(i,j):
            if i < 0 or j < 0 or i == rows or j == cols or board[i][j] != "O":
                return
            
            board[i][j] = "S"
            helper(i+1,j)
            helper(i-1, j)
            helper(i, j+1)
            helper(i,j-1)
        
        for c in range(cols):
            helper(0,c)
            helper(rows-1,c)
        for r in range(rows):
            helper(r,0)
            helper(r, cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"