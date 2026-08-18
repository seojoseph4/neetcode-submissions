class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm=defaultdict(int)
        l = 0
        r = 0
        res = 0
        maxF = 0

        while r < len(s):
            hm[s[r]]+=1
            maxF =  max(maxF, hm[s[r]])
            while (r-l+1) - maxF > k:
                hm[s[l]]-=1
                l+=1
            res = max(res, (r-l+1))
            r+=1
        
        return res


        