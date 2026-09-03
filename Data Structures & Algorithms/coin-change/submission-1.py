class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(t):
            if t == 0:
                return 0
            if t in memo:
                return memo[t]
            
            res = float("inf")
            for c in coins:
                if t - c >= 0:
                    res = min(res, 1+dfs(t-c))
            
            memo[t] = res
            return res
        res = dfs(amount)
        return -1 if res >= float("inf") else res
