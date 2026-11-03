class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag = set() #r-c
        ndiag = set() #r+c

        res = []
        curr = [["."]*n for _ in range(n)]

        def helper(r):
            if r >= n:
                res.append(["".join(row) for row in curr])
                return
            for c in range(n):
                if c in cols or (r-c) in diag or (r+c) in ndiag:
                    continue
                curr[r][c] = "Q"
                cols.add(c)
                diag.add(r-c)
                ndiag.add(r+c)
                helper(r+1)
                curr[r][c] = "."
                cols.remove(c)
                diag.remove(r-c)
                ndiag.remove(r+c)
        helper(0)
        return res