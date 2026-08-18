class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)
        res = 0
        for n in hs:
            if n-1 in hs:
                continue
            else:
                curr = n
                while curr+1 in hs:
                    curr+=1
                res = max(res, curr-n+1)
        return res

                    
        