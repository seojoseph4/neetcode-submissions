class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(o, c):
            if o == c == n:
                res.append("".join(curr))
                return
            if o == c:
                if o < n:
                    curr.append("(")
                    dfs(o+1,c)
                    curr.pop()
            else:
                if c < n:
                    curr.append(")")
                    dfs(o,c+1)
                    curr.pop()
                if o < n :
                    curr.append("(")
                    dfs(o+1,c)
                    curr.pop()
        dfs(0,0)
        return res
            