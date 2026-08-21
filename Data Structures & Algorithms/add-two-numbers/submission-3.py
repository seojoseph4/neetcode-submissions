# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode()
        
        carry = 0
        while l1 and l2:
            currval = (l1.val+ l2.val+carry)
            digit = currval % 10
            carry = currval // 10
            curr.next = ListNode(digit)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            currval = (v1+v2+carry)
            digit = currval % 10
            carry = currval //10
            curr.next = ListNode(digit)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res.next