class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            res = 0
            while num:
                digit = num% 10
                res += digit * digit
                num = num//10
            return res

        slow = n
        fast = helper(n)
        while fast!= 1 and slow !=fast:
            slow = helper(slow)
            fast =helper(helper(fast))
            
        
        return fast == 1
        