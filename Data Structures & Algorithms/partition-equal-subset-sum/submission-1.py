class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        goal = 0
        for n in nums:
            goal+=n
        
        if goal %2 == 1:
            return False
        
        goal = goal/2
        dp = set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            nextdp = set()
            for t in dp:
                if (t+nums[i]) == goal:
                    return True
                nextdp.add(t+nums[i])
                nextdp.add(t)
            dp = nextdp
        
        return False

        
        