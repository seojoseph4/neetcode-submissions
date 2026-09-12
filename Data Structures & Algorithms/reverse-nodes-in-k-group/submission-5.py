# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prevGroupTail = ListNode(0, head)
        kth = head
        res = None
        while True:
            i = 1
            while kth and i < k:
                kth = kth.next
                i+=1
            
            if not kth:
                return res
            nextGroupHead = kth.next

            prev = nextGroupHead
            curr = prevGroupTail.next
            save = prevGroupTail.next
            while curr != nextGroupHead:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if not res:
                res = kth
            prevGroupTail.next = kth
            kth = nextGroupHead
            prevGroupTail = save


