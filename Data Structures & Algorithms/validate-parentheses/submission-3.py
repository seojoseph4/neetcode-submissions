class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for p in s:
            if p not in mapping:
                stack.append(p)
            else:
                if stack and mapping[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0