# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        curr = res
        carry =0
        while l1 or l2 or carry:
            if l1:
                one = l1.val
                l1 = l1.next
            else:
                one = 0
            if l2:
                two = l2.val
                l2 = l2.next
            else:
                two =0
            val = one+two+carry
            carry = val //10
            digit = val %10
            print(carry, digit, val)
            temp = ListNode(digit)
            curr.next = temp
            curr = curr.next
        
        return res.next