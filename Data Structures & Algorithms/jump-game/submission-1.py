class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp = [False]*(len(nums))

        # dp[-1] = True
        flag = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] + i >= flag:
                flag = i
            
        print(flag)
        return flag == 0
        