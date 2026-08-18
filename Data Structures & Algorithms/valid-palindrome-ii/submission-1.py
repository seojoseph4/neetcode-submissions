class Solution:
    def helper(self, s):
        l = 0
        r = len(s)-1
        while l <r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        counter = 0
        while l <r:
            if s[l] != s[r]:
                if counter > 0:
                    return False
                else:
                    if self.helper(s[l+1:r+1]):
                        return True
                    if self.helper(s[l:r]):
                        return True
                    return False
            l+=1
            r-=1
        return True
        