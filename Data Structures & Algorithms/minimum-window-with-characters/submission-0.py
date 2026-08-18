class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        minlen = len(s) +1
        res = ""
        hm = {}
        for char in t:
            if char in hm:
                hm[char] +=1
            else:
                hm[char] = 1
        
        needed = len(t)
        while r < len(s):
            while needed > 0 and r < len(s):
                if s[r] in hm:
                    if hm[s[r]] > 0:
                        needed -=1
                    hm[s[r]] -=1
                r+=1


            while needed < 1:
                if r- l < minlen:
                    minlen = r-l
                    res = s[l:r]
                if s[l] in hm:
                    hm[s[l]] +=1
                    if hm[s[l]] > 0:
                        needed+=1

                l+=1
        return res



        

        