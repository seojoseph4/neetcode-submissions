class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ndiag = set() # (c-r)
        diag = set() # (r+c)
        cols = set()
        res = []
        curr = []
        board = [["."]*n for i in range(n)]
        def helper(r):
            if r == n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in diag or (c-r) in ndiag:
                    continue
                
                ndiag.add(c-r)
                diag.add(c+r)
                cols.add(c)
                board[r][c] = "Q"
                helper(r+1)
                board[r][c] = "."
                ndiag.remove(c-r)
                diag.remove(c+r)
                cols.remove(c)
        helper(0)
        return res
