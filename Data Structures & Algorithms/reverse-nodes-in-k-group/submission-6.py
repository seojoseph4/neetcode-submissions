# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        

        prevGroupTail = ListNode()
        prevGroupTail.next = head
        kth = head
        res = None
        while True:
            #kth node
            gap = 1

            while kth and gap < k:
                kth = kth.next
                gap+=1
            gap = 0

            if not kth:
                break
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
        return res
        



