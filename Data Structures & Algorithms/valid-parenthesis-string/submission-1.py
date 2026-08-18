class Solution:
    def checkValidString(self, s: str) -> bool:
        stackopens = []
        stackstars = []
        for i,c in enumerate(s):
            if c == "(":
                stackopens.append(i)
            if c == "*":
                stackstars.append(i)
            if c == ")":
                if stackopens:
                    stackopens.pop()
                elif stackstars:
                    stackstars.pop()
                else:
                    return False
        while stackopens:
            if stackstars:
                opens = stackopens.pop()
                stars= stackstars.pop()
                if stars < opens:
                    return False
            else:
                return False
        return True
                    
