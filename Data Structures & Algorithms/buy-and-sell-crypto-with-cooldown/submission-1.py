class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #decision when not have stock
        #buy skip

        #deicison when have stock
        #hold or sell

        memo = {}
        def helper(i, havestock):
            if i >= len(prices):
                return 0
            if (i,havestock) in memo:
                return memo[(i, havestock)]
            if havestock:
                res = max(helper(i+1, True), helper(i+2, False) + prices[i])

            else:
                res = max(helper(i+1, True) - prices[i], helper(i+1, False))
            
            memo[(i,havestock)] = res
            return res

        return helper(0, False)