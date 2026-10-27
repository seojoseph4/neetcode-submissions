class Solution:
    def checkValidString(self, s: str) -> bool:
        opens =[]
        stars =[]

        for i in range(len(s)):
            if s[i] == "(":
                opens.append(i)
            elif s[i] == "*":
                stars.append(i)
            else:
                if opens:
                    opens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            
        while opens and stars:
            if opens[-1] < stars[-1]:
                opens.pop()
                stars.pop()
            else:
                break
        
        return len(opens) == 0

