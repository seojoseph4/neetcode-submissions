class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, curr, subset):
            if curr == target:
                res.append(subset[:])
            for j in range(i, len(nums)):
                if curr+nums[j] > target:
                    break
                subset.append(nums[j])
                dfs(j, curr+nums[j], subset)
                subset.pop()

        dfs(0, 0, [])
        return res
