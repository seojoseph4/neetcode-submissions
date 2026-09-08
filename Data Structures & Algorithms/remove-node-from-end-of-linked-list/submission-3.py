# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = ListNode(0, head)
        res = slow
        fast = head
        gap = 1
        while gap <= n:
            fast = fast.next if fast else None
            gap+=1
        while fast:
            slow = slow.next
            fast = fast.next
        print(slow.val)
        slow.next = slow.next.next

        return res.next

        
        