class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        memo = {}
        def helper(i, runsum):
            if runsum > amount:
                return 0 
            if runsum == amount:
                return 1
            
            if (i, runsum) in memo:
                return memo[(i, runsum)]
            
            res = 0
            for j in range(i, len(coins)):
                res+= helper(j, runsum+coins[j])
            
            memo[(i, runsum)] = res

            return res
        
        return helper(0,0)
