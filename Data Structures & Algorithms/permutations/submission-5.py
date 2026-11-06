class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    curr.append(nums[i])
                    helper(curr)
                    seen.remove(i)
                    curr.pop()
                
        helper([])
        return res