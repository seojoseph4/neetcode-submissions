class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        #slow traveled a+ b
        # a is the distance traveled outside the loop
        # b is the distance traveled within the loop

        #fast traveled 2* (a+b)
        # the extra distance fast traveled is a+b, which is equal to some number of loops m*c

        #a+b = M*c

        #so this means going forward a amount would bring to start of cycle

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        
        