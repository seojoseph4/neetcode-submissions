class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        carry = 1
        for i in range(len(digits)-1,-1,-1):

            d = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            res.append(d)
        #     print(digits[i],carry)

        # print(carry)
        if carry == 1:
            res.append(carry)

        res.reverse()
        return res

        