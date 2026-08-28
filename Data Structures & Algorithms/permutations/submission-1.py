class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        curr = []
        p = [False for _ in range(len(nums))]

        def bt(picked):
            if len(curr) == len(nums):
                res.append(curr.copy())
            
            for j in range(len(nums)):
                if picked[j]:
                    continue
                curr.append(nums[j])
                picked[j] = True
                bt(picked)
                curr.pop()
                picked[j] = False
        bt(p)
        return res