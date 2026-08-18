class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        res = 0
        l = 0
        r = 0
        currMax = 0
        while r < len(s):
            if s[r] in hm:
                hm[s[r]] +=1
            else:
                hm[s[r]] = 1
            currMax = max(currMax, hm[s[r]])
            while l < r and (r-l+1)-currMax > k:
                hm[s[l]] -=1
                l+=1
            res = max(res, r-l+1 )
            r+=1
        return res

        