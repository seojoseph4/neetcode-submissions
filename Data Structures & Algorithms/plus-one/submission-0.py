class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        p = len(digits)-1
        
        val  = (digits[p] + 1) % 10
        carry = (digits[p]+1) // 10

        res.append(val)
        p-=1
        while carry and p >= 0:
            temp = (digits[p]+carry)
            val = temp%10
            carry = temp //10
            res.append(val)
            p-=1
        while p >=0:
            res.append(digits[p])
            p-=1
        if carry != 0:
            res.append(carry)
        return res[::-1]
        
        

        
        