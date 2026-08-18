class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+','-','*','/']
        nums = []
        for tok in tokens:
            # print(nums)
            if tok in operations:
                two = int(nums.pop())
                one = int(nums.pop())
                if tok == '+':
                    nums.append(str(one+two))
                elif tok == '-':
                    nums.append(str(one-two))
                elif tok == '*':
                    nums.append(str(one*two))
                elif tok == '/':
                    nums.append(str(int((one/two))))
            else:
                nums.append(tok)
        return int(nums[-1])

            

        