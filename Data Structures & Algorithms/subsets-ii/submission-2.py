class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        curr = []

        def bt(i):
            res.append(curr[:])
            for j in range(i, len(nums)):
                if j > i and nums[j-1] == nums[j]:
                    continue
                curr.append(nums[j])
                bt(j+1)
                curr.pop()

        bt(0)
        return res