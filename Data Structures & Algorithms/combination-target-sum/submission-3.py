class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res= []
        curr = []
        def bt(index, runsum):
            if index == len(nums):
                return
            if runsum == target:
                res.append(curr.copy())
            elif runsum > target:
                return
            
            for j in range(index, len(nums)):
                runsum+=nums[j]
                curr.append(nums[j])
                bt(j, runsum)
                runsum-=nums[j]
                curr.pop()
        bt(0,0)
        return res

