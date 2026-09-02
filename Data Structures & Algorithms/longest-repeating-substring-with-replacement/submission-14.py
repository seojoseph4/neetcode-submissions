class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxf = 0
        l = 0
        r = 0

        hm = defaultdict(int)
        res = 0

        while r < len(s):
            hm[s[r]]+=1
            maxf = max(maxf,hm[s[r]])

            while (r-l+1) - maxf > k:
                hm[s[l]]-=1
                if hm[s[l]] == 0:
                    del hm[s[l]]
                l+=1
            res = max(res, (r-l+1))
            r+=1
        
        return res
                
        