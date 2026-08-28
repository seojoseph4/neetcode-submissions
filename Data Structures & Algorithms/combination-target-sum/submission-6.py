class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res= []
        curr = []
        nums.sort()
        def bt(index, runsum):
            if runsum == target:
                res.append(curr.copy())
                return
            
            for j in range(index, len(nums)):
                if runsum + nums[j] > target:
                    return
                curr.append(nums[j])
                bt(j, runsum+ nums[j])
                curr.pop()
        bt(0,0)
        return res

