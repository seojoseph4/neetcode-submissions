class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res = 0
        memo = {}
        def dfs(i, currsum):
            if currsum == amount:
                return 1
            if i == len(coins):
                return 0
            if currsum > amount:
                return 0
            if (i, currsum) in memo:
                return memo[(i,currsum)]
            result = dfs(i+1, currsum) + dfs(i, currsum+coins[i])
            memo[(i,currsum)] = result
            return result

        return dfs(0,0)



