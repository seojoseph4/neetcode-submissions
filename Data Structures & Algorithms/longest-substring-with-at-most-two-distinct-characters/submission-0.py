class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hm = {}

        l = 0
        r = 0
        res = 0
        #char:lastseenindex
        for r in range(len(s)):
            hm[s[r]] = r
            if len(hm.keys()) > 2:
                minkey = None
                minVal = float("inf")
                for key,val in hm.items():
                    if val <minVal:
                        minVal = val
                        minKey = key
                
                l = minVal+1
                del hm[minKey]
            
            res = max(res, r-l+1)
        
        return res

