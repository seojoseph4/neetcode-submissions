class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check  = set()
        res = 0
        for num in nums:
            check.add(num)
        
        for i in nums:
            currCount = 0
            if i-1 in check:
                continue
            else:
                curr = i
                currCount+=1
                while curr+1 in check:
                    currCount+=1
                    curr = curr+1

            res = max(res, currCount)

        return res
            
                    
        