class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def helper(i):
            res = 0
            start = 0
            #odd
            l, r = i,i
            while l >=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            length = (r-1)-(l+1)+1
            if length > res:
                res = length
                start = l+1

            #even
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l]==s[r]:
                l-=1
                r+=1
            length = (r-1)-(l+1)+1
            if length > res:
                res = length
                start = l+1
            return res, start
        res = 0
        resI = 0
        for i in range(len(s)):
            mlength, st = helper(i)
            # print(i, temp)
            if mlength > res:
                res = mlength
                resI = st
        # print(res,resI)
        if res ==0:
            return ""
        else:
            return s[resI:resI+res]

