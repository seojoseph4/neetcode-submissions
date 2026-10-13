class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i, ch in enumerate(s):
            hm[ch] = i
        
        
        l = 0
        r = 0
        maxwindow = 0
        res = []
        while r < len(s):
            maxwindow = max(maxwindow,hm[s[r]])
            if r == maxwindow:
                res.append(r-l+1)
                r+=1
                l = r
                maxwindow = 0
                continue
            
            r+=1
        
        return res

