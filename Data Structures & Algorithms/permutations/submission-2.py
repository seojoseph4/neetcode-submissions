class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        curr = []

        def dfs(added):
            if len(curr) == len(nums):
                res.append(curr[:])
                return

            for i in range(len(nums)):
                if i not in added:
                    curr.append(nums[i])
                    added.add(i)
                    dfs(added)
                    curr.pop()
                    added.remove(i)
        seen = set()
        dfs(seen)
        return res
            
