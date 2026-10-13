class Solution:
    def checkValidString(self, s: str) -> bool:
        pcount = []
        stars = []
    
        for i,ch in enumerate(s):
            if ch == "(":
                pcount.append(i)
            if ch == ")":
                if pcount:
                    pcount.pop()
                else:
                    if stars:
                        stars.pop()
                    else:
                        return False
            if ch == "*":
                stars.append(i)

            
        while pcount and stars:
            if stars[-1] > pcount[-1]:
                stars.pop()
                pcount.pop()
            else:
                return False
        
        return not pcount