class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        digits[-1] +=1
        for i in range(len(digits)-1,-1,-1):
            d = digits[i] + carry
            carry = d //10
            d = d % 10
            res.append(d)
        
        if carry != 0:
            res.append(carry)
        
        
        return res[::-1]