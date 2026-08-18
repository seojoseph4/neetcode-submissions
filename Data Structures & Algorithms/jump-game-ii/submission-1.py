class Solution:
    def jump(self, nums: List[int]) -> int:
        
        pre = [float("inf")]*len(nums)
        pre[len(nums)-1] = 0
        for i in range(len(nums)-2,-1,-1):
            for j in range(i+1, min(i+1+nums[i], len(nums))):
                pre[i] = min(pre[i], pre[j]+1)
        return pre[0]
            





        