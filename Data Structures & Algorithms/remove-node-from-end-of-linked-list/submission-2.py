# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 1
        res = prev = ListNode(0,head)
        while i < n:
            head = head.next
            i+=1
        while head.next:
            head = head.next
            prev = prev.next
        prev.next = prev.next.next
        # print(head.val if head else 0)
        # print(prev.val if prev else 0)
        return res.next
        