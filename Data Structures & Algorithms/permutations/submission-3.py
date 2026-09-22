class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        seen = set()

        def helper(seen):
            if len(seen) == len(nums):
                res.append(curr[:])
                return
            for j in range(len(nums)):
                if j not in seen:
                    seen.add(j)
                    curr.append(nums[j])
                    helper(seen)
                    curr.pop()
                    seen.remove(j)
        helper(seen)
        return res

            

