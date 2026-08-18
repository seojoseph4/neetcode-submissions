class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ['+','-','*','/']
        nums = []
        for element in tokens:
            print(nums)
            if element not in operations:
                nums.append(int(element))
            else:
                if element == "+":
                    curr = nums.pop() + nums.pop()
                elif element == "-":
                    a = nums.pop()
                    b = nums.pop()
                    curr = b-a
                elif element == "*":
                    a = nums.pop()
                    b = nums.pop()
                    curr = b*a
                elif element == "/":
                    a = nums.pop()
                    b = nums.pop()
                    curr = int(b/a)
                nums.append(curr)
                print(curr)
        return nums[0]
                    
                    
            

        