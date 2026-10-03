class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diag = set() # (c-r)
        ndiag = set() # (r+c)
        cols = set()
        res = []
        board = [["."]*n for _ in range(n)]
        def helper(r):
            if r >=n:
                res.append(["".join(i) for i in board])
                return 
            for c in range(n):
                if (c-r) in diag or (c+r) in ndiag or c in cols:
                    continue
                board[r][c] = "Q"
                diag.add(c-r)
                ndiag.add(c+r)
                cols.add(c)
                helper(r+1)
                board[r][c] = "."
                diag.remove(c-r)
                ndiag.remove(c+r)
                cols.remove(c)
                
        helper(0)
        return res