class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        curr = []

        def bt(i):
            nonlocal curr
            res.append(curr.copy())
            
            for j in range(i, len(nums)):
                curr.append(nums[j])
                bt(j+1)
                curr.pop()
        bt(0)
        return res