class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        memo = {}
        def helper(i, runsum):
            if i  == len(coins):
                return 0
            if runsum > amount:
                return 0 
            if runsum == amount:
                return 1
            
            if (i, runsum) in memo:
                return memo[(i, runsum)]
            

            take = helper(i, runsum+coins[i])
            notake = helper(i+1, runsum)
            
            memo[(i, runsum)] = take+notake

            return memo[(i,runsum)]
        
        return helper(0,0)
