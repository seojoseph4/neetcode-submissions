class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIn = 0
        resLen = 0

        for i in range(len(s)):
            #odd
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r-l +1
                if currLen > resLen:
                    resLen = currLen
                    resIn = l
                l-=1
                r+=1
                            

            #even
            l = i
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                currLen = r-l +1
                if currLen > resLen:
                    resLen = currLen
                    resIn = l
                l-=1
                r+=1
        return s[resIn:resIn+resLen]

        