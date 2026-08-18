class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastindex = {}

        for i in range(len(s)):
            lastindex[s[i]] = i

        l = 0
        r = 0
        curr = 0
        res= []
        while curr < len(s) and r < len(s):
            r = max(r, lastindex[s[curr]])
            if curr < r:
                curr+=1   
            else:
                res.append(r-l+1)
                print(res)
                curr = r+1
                l = r+1
        
        return res


        