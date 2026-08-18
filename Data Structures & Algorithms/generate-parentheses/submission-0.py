class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def dfs(opens, closeds, stack):
            nonlocal res
            if opens == n and closeds == n:
                res.append("".join(stack))
                return
            
            if opens < n:
                stack.append("(")
                
                dfs(opens+1, closeds, stack)
                stack.pop()

            if closeds < n and opens > closeds:
                stack.append(")")
                
                dfs(opens, closeds+1, stack)
                stack.pop()
            
            return
        
        dfs(0, 0, [])
        return res
