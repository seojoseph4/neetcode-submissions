class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def helper(n, seen):
            if n in seen:
                return False
            else:
                seen.add(n)
            newn = 0
            while n > 0:
                digit = n%10
                n = n//10
                newn += digit*digit
            
            if newn == 1:
                return True
            else:
                return helper(newn, seen)
        return helper(n, seen)
        