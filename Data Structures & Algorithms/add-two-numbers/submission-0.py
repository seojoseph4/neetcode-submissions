# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1:
            num1 = str(l1.val) + num1
            l1 = l1.next
        while l2:
            num2 = str(l2.val) + num2
            l2 = l2.next
        print(num1)
        print(num2)
        add = str(int(num1) + int(num2))
        curr = ListNode(int(add[-1]))
        res = curr

        for d in range(len(add)-2,-1,-1):
            temp = ListNode(int(add[d]))
            curr.next = temp
            curr = curr.next
            print(add[d])

        print(add)
        return res