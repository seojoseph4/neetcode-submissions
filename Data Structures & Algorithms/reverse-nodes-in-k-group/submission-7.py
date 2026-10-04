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
            gap = 1
            while kth and gap < k:
                kth = kth.next
                gap+=1
            if not kth:
                break
                
            nextGroupHead = kth.next
            curr = prevGroupTail.next
            prev = nextGroupHead
            save = curr
            while curr!= nextGroupHead:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            if not res:
                res = kth
            prevGroupTail.next = kth
            prevGroupTail = save
            kth = nextGroupHead
        return res


            