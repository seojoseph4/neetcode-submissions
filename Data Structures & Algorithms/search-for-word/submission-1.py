class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res =  False
        def dfs(row, col, curr):
            if curr == len(word):
                return True
            if row < 0 or col <0 or row >= len(board) or col >= len(board[0]) or word[curr] != board[row][col]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'

            found = (dfs(row, col+1, curr+1) or
            dfs(row, col-1, curr+1) or
            dfs(row+1, col, curr+1) or
            dfs(row-1, col, curr+1))

            board[row][col] = temp
            return found

        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False

        