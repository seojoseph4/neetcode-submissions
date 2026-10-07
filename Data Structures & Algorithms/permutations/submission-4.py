class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        seen = set()
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue
                curr.append(nums[i])
                seen.add(nums[i])
                helper(curr)
                seen.remove(nums[i])
                curr.pop()
        
        helper([])
        return res