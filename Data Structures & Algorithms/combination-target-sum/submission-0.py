class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, curr):
            if curr == target:
                res.append(subset.copy())
                return
            if i >= len(nums) or curr > target:
                return
            
            subset.append(nums[i])
            curr +=nums[i]
            dfs(i, curr)

            subset.pop()
            curr -=nums[i]
            dfs(i+1, curr)

        dfs(0, 0)
        return res