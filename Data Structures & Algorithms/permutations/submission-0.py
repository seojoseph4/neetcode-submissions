class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(subset, seen):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if seen[i] == True:
                    continue
                subset.append(nums[i])
                seen[i] = True
                dfs(subset, seen)
                subset.pop()
                seen[i] = False


        
        dfs([],[False]*len(nums))
        return res

        